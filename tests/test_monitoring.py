from backend.monitoring.baseline import compare_snapshots, create_snapshot
from backend.monitoring.metrics_analyzer import analyze_changes
from backend.monitoring.log_collector import normalize_log, summarize_logs


def test_snapshot_comparison_computes_numeric_delta():
    baseline = create_snapshot({"checkout_latency_ms": 100, "requests": 10})
    current = create_snapshot({"checkout_latency_ms": 145, "requests": 12})

    result = compare_snapshots(baseline, current)
    assert result["changes"]["checkout_latency_ms"]["delta"] == 45
    assert result["changes"]["requests"]["delta"] == 2


def test_analyzer_flags_increased_latency():
    result = analyze_changes({
        "changes": {
            "checkout_latency_ms": {
                "baseline": 100,
                "current": 150,
                "delta": 50,
            }
        }
    })
    assert result["observation_count"] == 1
    assert result["observations"][0]["observation"] == "Latency increased"


def test_log_summary_counts_errors():
    logs = [
        normalize_log("request completed", "store-api", "INFO"),
        normalize_log("payment failed", "store-api", "ERROR"),
    ]
    result = summarize_logs(logs)
    assert result["total_logs"] == 2
    assert result["error_count"] == 1
