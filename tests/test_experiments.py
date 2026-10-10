
from backend.experiments.runner import run_experiment


def test_runner_does_not_inject_real_fault():
    result = run_experiment(
        "dependency_delay",
        "payment-mock",
        5,
    )

    assert result["mode"] == "simulation"
    assert result["action_executed"] is False
    assert result["recovery_status"] == "not_required"
