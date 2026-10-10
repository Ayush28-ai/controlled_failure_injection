
from datetime import datetime, timezone

from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "bosch-backend",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
