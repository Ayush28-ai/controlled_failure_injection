
from fastapi import APIRouter, HTTPException

from backend.monitoring.prometheus_client import (
    APPROVED_QUERIES,
    query_prometheus,
)

router = APIRouter(prefix="/metrics", tags=["Metrics"])


@router.get("")
def available_metrics():
    return {
        "available_metrics": list(APPROVED_QUERIES.keys())
    }


@router.get("/{metric_name}")
async def get_metric(metric_name: str):
    if metric_name not in APPROVED_QUERIES:
        raise HTTPException(
            status_code=404,
            detail="Unknown metric",
        )

    try:
        data = await query_prometheus(metric_name)
        return {"metric": metric_name, "data": data}
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail="Unable to query Prometheus",
        ) from exc
