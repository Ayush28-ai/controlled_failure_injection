
def describe(target_service: str) -> dict:
    return {
        "scenario": "dependency_delay",
        "target_service": target_service,
        "expected_risk": "Downstream latency may increase request latency.",
        "execution_mode": "simulation",
    }
