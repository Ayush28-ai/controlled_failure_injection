import asyncio

import pytest

from backend.safety.recovery import recover_experiment
from backend.safety.watchdog import run_with_timeout


def test_simulation_recovery_requires_no_rollback():
    result = asyncio.run(
        recover_experiment(experiment_id=1, simulation_mode=True)
    )
    assert result["status"] == "not_required"
    assert result["simulation_mode"] is True


def test_real_recovery_is_not_enabled():
    with pytest.raises(RuntimeError, match="not implemented"):
        asyncio.run(
            recover_experiment(experiment_id=1, simulation_mode=False)
        )


def test_watchdog_returns_operation_result():
    async def operation():
        return "done"

    assert asyncio.run(run_with_timeout(operation, 1)) == "done"


def test_watchdog_times_out_slow_operation():
    async def operation():
        import asyncio
        await asyncio.sleep(0.1)

    with pytest.raises(TimeoutError):
        asyncio.run(run_with_timeout(operation, 0.01))


def test_watchdog_rejects_non_positive_timeout():
    async def operation():
        return None

    with pytest.raises(ValueError, match="positive"):
        asyncio.run(run_with_timeout(operation, 0))
