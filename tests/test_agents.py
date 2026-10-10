
from backend.agents.experiment_planner import ExperimentPlanner


def test_checkout_symptom_selects_dependency_delay():
    plan = ExperimentPlanner().propose(
        "Checkout is slow because payment is delayed"
    )

    assert plan["scenario"] == "dependency_delay"
    assert plan["target_service"] == "payment-mock"


def test_planner_returns_simulation_mode():
    plan = ExperimentPlanner().propose(
        "The application has high traffic"
    )

    assert plan["mode"] == "simulation"
