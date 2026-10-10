
from backend.experiments.registry import list_scenarios


class ExperimentPlanner:
    def propose(self, symptom: str) -> dict:
        text = symptom.lower()

        if "checkout" in text or "payment" in text:
            scenario = "dependency_delay"
            target = "payment-mock"
            reason = (
                "Investigate checkout sensitivity to dependency latency."
            )

        elif "crash" in text or "unavailable" in text:
            scenario = "service_shutdown"
            target = "store-api"
            reason = (
                "Assess the impact of application unavailability."
            )

        else:
            scenario = "traffic_spike"
            target = "store-api"
            reason = (
                "Assess application behavior under increased demand."
            )

        return {
            "scenario": scenario,
            "target_service": target,
            "duration_seconds": 10,
            "rationale": reason,
            "mode": "simulation",
            "available_scenarios": [
                item["id"] for item in list_scenarios()
            ],
        }
