
from fastapi import APIRouter

from backend.orchestration.workflow import ExperimentWorkflow
from backend.schemas import PlanRequest

router = APIRouter(prefix="/planner", tags=["Planner"])
workflow = ExperimentWorkflow()


@router.post("/propose")
def propose_experiment(request: PlanRequest):
    return workflow.propose(request.symptom)
