from backend.agents.experiment_planner import ExperimentPlanner
from backend.agents.solutions_expert import SolutionsExpert


def test_checkout_symptom_selects_dependency_delay():
    plan = ExperimentPlanner().propose(
        "Checkout is slow because payment is delayed"
    )
    assert plan["scenario"] == "dependency_delay"
    assert plan["target_service"] == "payment-mock"
    assert plan["mode"] == "simulation"


def test_crash_symptom_selects_service_shutdown():
    plan = ExperimentPlanner().propose("The service crashed and is unavailable")
    assert plan["scenario"] == "service_shutdown"
    assert plan["target_service"] == "store-api"


def test_default_symptom_selects_traffic_spike():
    plan = ExperimentPlanner().propose("We need to test general capacity")
    assert plan["scenario"] == "traffic_spike"


def test_solution_expert_does_not_claim_root_cause_without_evidence():
    result = SolutionsExpert().recommend([])
    assert result["severity"] == "unknown"
    assert result["evidence"] == []
    assert "Insufficient evidence" in result["likely_cause"]


def test_solution_expert_marks_observations_for_review():
    observations = [{"metric": "checkout_latency_ms", "change": 120}]
    result = SolutionsExpert().recommend(observations)
    assert result["severity"] == "review_required"
    assert result["evidence"] == observations
