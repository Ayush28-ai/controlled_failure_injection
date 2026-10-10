
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.schemas import FindingCreate, FindingOut
from backend.storage.database import get_db
from backend.storage.repository import (
    create_finding,
    list_findings,
)

router = APIRouter(prefix="/findings", tags=["Findings"])


@router.get("", response_model=list[FindingOut])
def get_findings(
    limit: int = 50,
    db: Session = Depends(get_db),
):
    if not 1 <= limit <= 200:
        raise HTTPException(
            status_code=422,
            detail="limit must be between 1 and 200",
        )

    return list_findings(db, limit)


@router.post("", response_model=FindingOut, status_code=201)
def add_finding(
    request: FindingCreate,
    db: Session = Depends(get_db),
):
    if request.experiment_id is not None:
        from backend.storage.repository import get_experiment

        if get_experiment(db, request.experiment_id) is None:
            raise HTTPException(
                status_code=404,
                detail="Experiment not found",
            )

    return create_finding(
        db,
        title=request.title,
        severity=request.severity,
        evidence=request.evidence,
        recommendation=request.recommendation,
        experiment_id=request.experiment_id,
    )
