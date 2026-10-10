
import asyncio

from backend.safety.recovery import recover_experiment


def test_simulation_recovery_requires_no_rollback():
    result = asyncio.run(
        recover_experiment(
            experiment_id=1,
            simulation_mode=True,
        )
    )

    assert result["status"] == "not_required"
    assert result["simulation_mode"] is True
