
from backend.monitoring.baseline import compare_snapshots
from backend.monitoring.metrics_analyzer import analyze_changes


class MonitoringAgent:
    def analyze(
        self,
        baseline: dict,
        current: dict,
    ) -> dict:
        comparison = compare_snapshots(baseline, current)
        analysis = analyze_changes(comparison)

        return {
            "comparison": comparison,
            "analysis": analysis,
        }
