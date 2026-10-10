
from datetime import datetime, timezone

from backend.experiments.registry import get_scenario


def run_experiment(
    scenario: str,
    target_service: str,
    duration_seconds: int,
) -> dict:
    definition = get_scenario(scenario)

    if definition is None:
        raise ValueError("Unknown experiment scenario")

    if target_service not in definition["allowed_targets"]:
        raise ValueError(
            "Target is not permitted for this scenario"
        )

    # Simulation only: no Docker, network, or host changes.
    return {
        "mode": "simulation",
        "action_executed": False,
        "scenario": scenario,
        "target_service": target_service,
        "requested_duration_seconds": duration_seconds,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "recovery_status": "not_required",
        "message": (
            "Experiment recorded without injecting a real fault."
        ),
    }
