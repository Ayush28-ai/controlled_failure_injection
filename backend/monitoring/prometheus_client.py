import os
from typing import Any

import httpx


PROMETHEUS_URL = os.getenv(
    "PROMETHEUS_URL",
    "http://localhost:9090",
)

APPROVED_QUERIES: dict[str, str] = {
    "targets_up": "up",
    "http_requests": "bosch_http_requests_total",
    "http_request_rate": (
        "sum(rate(bosch_http_requests_total[1m]))"
    ),
    "container_cpu": (
        'rate(container_cpu_usage_seconds_total'
        '{container!=""}[1m])'
    ),
    "container_memory": (
        'container_memory_working_set_bytes'
        '{container!=""}'
    ),
}


class PrometheusError(RuntimeError):
    """Raised when Prometheus cannot return usable data."""


async def query_prometheus(
    query_name: str,
) -> dict[str, Any]:
    """Execute an approved Prometheus instant query."""
    if query_name not in APPROVED_QUERIES:
        raise ValueError(
            f"Unsupported Prometheus query: {query_name}"
        )

    query = APPROVED_QUERIES[query_name]
    url = f"{PROMETHEUS_URL.rstrip('/')}/api/v1/query"

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(
                url,
                params={"query": query},
            )
            response.raise_for_status()
            payload = response.json()

    except (httpx.HTTPError, ValueError) as exc:
        raise PrometheusError(
            f"Unable to query Prometheus: {exc}"
        ) from exc

    if not isinstance(payload, dict):
        raise PrometheusError(
            "Prometheus returned an invalid response"
        )

    if payload.get("status") != "success":
        raise PrometheusError(
            "Prometheus returned an unsuccessful query response"
        )

    data = payload.get("data")
    if not isinstance(data, dict):
        raise PrometheusError(
            "Prometheus response did not contain valid data"
        )

    return data


async def get_metric_summary() -> dict[str, Any]:
    """Collect dashboard metrics without treating missing data as zero."""
    summary: dict[str, Any] = {}

    for metric_name in (
        "targets_up",
        "http_requests",
        "http_request_rate",
    ):
        try:
            data = await query_prometheus(metric_name)
            summary[metric_name] = {
                "available": True,
                "result": data.get("result", []),
            }
        except (PrometheusError, ValueError) as exc:
            summary[metric_name] = {
                "available": False,
                "error": str(exc),
                "result": [],
            }

    return summary
