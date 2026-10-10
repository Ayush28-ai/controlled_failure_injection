
from sqlalchemy.orm import Session

from backend.experiments.runner import run_experiment
from backend.safety.guardrails import validate_experiment
from backend.storage.repository import create_experiment


def execute_simulation(db: Session, request) -> dict:
    validate_experiment(
        request.scenario,
        request.target_service,
        request.duration_seconds,
    )

    result = run_experiment(
        request.scenario,
        request.target_service,
        request.duration_seconds,
    )

    record = create_experiment(
        db,
        scenario=request.scenario,
        target_service=request.target_service,
        duration_seconds=request.duration_seconds,
        rationale=request.rationale,
        result=result,
        status="completed",
        simulation_mode=True,
    )

    return {
        "experiment": record,
        "result": result,
    }
