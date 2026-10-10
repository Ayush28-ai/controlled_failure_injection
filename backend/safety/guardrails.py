
import os

from fastapi import HTTPException


MAX_DURATION = int(
    os.getenv("MAX_EXPERIMENT_DURATION_SECONDS", "30")
)

ALLOWED_SCENARIOS = {
    "service_shutdown",
    "dependency_delay",
    "traffic_spike",
}

# These IDs are examples. Match them to the verified topology.
ALLOWED_TARGETS = {
    "store-api",
    "payment-mock",
}


def validate_experiment(
    scenario: str,
    target_service: str,
    duration_seconds: int,
) -> None:
    if scenario not in ALLOWED_SCENARIOS:
        raise HTTPException(
            status_code=422,
            detail="Experiment scenario is not allow-listed",
        )

    if target_service not in ALLOWED_TARGETS:
        raise HTTPException(
            status_code=422,
            detail="Target service is not allow-listed",
        )

    if not 1 <= duration_seconds <= min(MAX_DURATION, 30):
        raise HTTPException(
            status_code=422,
            detail="Duration exceeds the permitted limit",
        )

    if os.getenv("EXPERIMENT_MODE", "simulation") != "simulation":
        raise HTTPException(
            status_code=503,
            detail=(
                "Real fault injection is not enabled in this build"
            ),
        )
