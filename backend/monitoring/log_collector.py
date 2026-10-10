
from datetime import datetime, timezone


def normalize_log(
    message: str,
    service: str,
    level: str = "INFO",
) -> dict:
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "service": service,
        "level": level.upper(),
        "message": message[:4000],
    }


def summarize_logs(logs: list[dict]) -> dict:
    error_logs = [
        log for log in logs
        if log.get("level", "").upper() in {
            "ERROR", "CRITICAL"
        }
    ]

    return {
        "total_logs": len(logs),
        "error_count": len(error_logs),
        "errors": error_logs[:50],
    }
