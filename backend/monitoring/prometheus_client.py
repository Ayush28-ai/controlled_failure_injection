
import os

import httpx


PROMETHEUS_URL = os.getenv(
    "PROMETHEUS_URL",
    "http://localhost:9090",
)

# Only expose queries explicitly approved by the application.
APPROVED_QUERIES = {
    "targets_up": "up",
    "http_requests": "bosch_http_requests_total",
    "container_cpu": (
        'sum(rate(container_cpu_usage_seconds_total[5m]))'
    ),
    "container_memory": (
        "sum(container_memory_working_set_bytes)"
    ),
}


async def query_prometheus(metric_name: str) -> dict:
    if metric_name not in APPROVED_QUERIES:
        raise ValueError("Metric is not allow-listed")

    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get(
            f"{PROMETHEUS_URL.rstrip('/')}/api/v1/query",
            params={"query": APPROVED_QUERIES[metric_name]},
        )
        response.raise_for_status()

    payload = response.json()

    if payload.get("status") != "success":
        raise RuntimeError("Prometheus query failed")

    return payload["data"]
