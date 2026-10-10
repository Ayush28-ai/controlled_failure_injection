
class SolutionsExpert:
    def recommend(self, observations: list[dict]) -> dict:
        if not observations:
            return {
                "severity": "unknown",
                "likely_cause": "Insufficient evidence",
                "evidence": [],
                "recommendation": (
                    "Collect valid baseline, experiment, and "
                    "recovery measurements before diagnosing."
                ),
            }

        return {
            "severity": "review_required",
            "likely_cause": "One or more metrics changed",
            "evidence": observations,
            "recommendation": (
                "Investigate the affected service and its "
                "dependencies. Verify the cause against logs "
                "and repeatable measurements before applying a fix."
            ),
        }
