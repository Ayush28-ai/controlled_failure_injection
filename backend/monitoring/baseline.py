
from datetime import datetime, timezone


def create_snapshot(metrics: dict) -> dict:
    return {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "metrics": metrics,
    }


def compare_snapshots(
    baseline: dict,
    current: dict,
) -> dict:
    baseline_metrics = baseline.get("metrics", {})
    current_metrics = current.get("metrics", {})

    changes = {}

    for name, current_value in current_metrics.items():
        baseline_value = baseline_metrics.get(name)

        if (
            isinstance(baseline_value, (int, float))
            and isinstance(current_value, (int, float))
        ):
            changes[name] = {
                "baseline": baseline_value,
                "current": current_value,
                "delta": current_value - baseline_value,
            }

    return {
        "baseline_captured_at": baseline.get("captured_at"),
        "current_captured_at": current.get("captured_at"),
        "changes": changes,
    }
