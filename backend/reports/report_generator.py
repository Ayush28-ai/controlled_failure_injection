
from datetime import datetime, timezone


def generate_report(
    experiment: dict,
    findings: list[dict],
) -> dict:
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "experiment": experiment,
        "findings": findings,
        "conclusion": (
            "Simulation report. Conclusions should be verified "
            "against actual application measurements."
        ),
    }
