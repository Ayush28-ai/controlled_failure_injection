
def describe(target_service: str) -> dict:
    return {
        "scenario": "service_shutdown",
        "target_service": target_service,
        "expected_risk": "Requests may fail if this service is unavailable.",
        "execution_mode": "simulation",
    }
