
from fastapi import APIRouter, HTTPException

from backend.safety.recovery import recover_experiment

router = APIRouter(prefix="/recovery", tags=["Recovery"])


@router.post("/{experiment_id}")
async def recover(experiment_id: int):
    if experiment_id < 1:
        raise HTTPException(
            status_code=422,
            detail="Invalid experiment ID",
        )

    # Recovery is a no-op because experiments are simulation-only.
    return await recover_experiment(
        experiment_id,
        simulation_mode=True,
    )
