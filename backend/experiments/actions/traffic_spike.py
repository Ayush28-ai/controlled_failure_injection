
def describe(target_service: str) -> dict:
    return {
        "scenario": "traffic_spike",
        "target_service": target_service,
        "expected_risk": "Increased demand may raise latency or errors.",
        "execution_mode": "simulation",
    }
