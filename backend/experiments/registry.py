
SCENARIOS = {
    "service_shutdown": {
        "name": "Service Shutdown Simulation",
        "description": "Model the loss of a service.",
        "allowed_targets": ["store-api"],
        "default_duration_seconds": 10,
    },
    "dependency_delay": {
        "name": "Dependency Delay Simulation",
        "description": "Model a slow downstream dependency.",
        "allowed_targets": ["payment-mock"],
        "default_duration_seconds": 10,
    },
    "traffic_spike": {
        "name": "Traffic Spike Simulation",
        "description": "Model an increase in incoming demand.",
        "allowed_targets": ["store-api"],
        "default_duration_seconds": 10,
    },
}


def list_scenarios() -> list[dict]:
    return [
        {"id": scenario_id, **details}
        for scenario_id, details in SCENARIOS.items()
    ]


def get_scenario(scenario_id: str) -> dict | None:
    return SCENARIOS.get(scenario_id)
