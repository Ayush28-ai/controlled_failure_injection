
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api.routes.health import router as health_router
from backend.orchestration.run_manager import execute_simulation
from backend.schemas import ExperimentCreate, ExperimentOut
from backend.storage.database import get_db
from backend.storage.repository import (
    get_experiment,
    list_experiments,
)

router = APIRouter(prefix="/experiments", tags=["Experiments"])


@router.post("", response_model=ExperimentOut, status_code=201)
def create_experiment(
    request: ExperimentCreate,
    db: Session = Depends(get_db),
):
    result = execute_simulation(db, request)
    return result["experiment"]


@router.get("", response_model=list[ExperimentOut])
def get_experiments(
    limit: int = 50,
    db: Session = Depends(get_db),
):
    if not 1 <= limit <= 200:
        raise HTTPException(
            status_code=422,
            detail="limit must be between 1 and 200",
        )

    return list_experiments(db, limit)


@router.get("/{experiment_id}", response_model=ExperimentOut)
def get_experiment_by_id(
    experiment_id: int,
    db: Session = Depends(get_db),
):
    record = get_experiment(db, experiment_id)

    if record is None:
        raise HTTPException(
            status_code=404,
            detail="Experiment not found",
        )

    return record
