
def analyze_changes(comparison: dict) -> dict:
    observations = []

    for name, values in comparison.get("changes", {}).items():
        baseline = values["baseline"]
        current = values["current"]
        delta = values["delta"]

        if name.endswith("_error_rate"):
            if current > baseline:
                observations.append({
                    "metric": name,
                    "change": delta,
                    "observation": "Error rate increased",
                })

        elif name.endswith("_latency_ms"):
            if current > baseline:
                observations.append({
                    "metric": name,
                    "change": delta,
                    "observation": "Latency increased",
                })

    return {
        "observations": observations,
        "observation_count": len(observations),
        "note": (
            "These observations compare supplied measurements. "
            "They do not establish root cause by themselves."
        ),
    }
