
from backend.agents.experiment_planner import ExperimentPlanner
from backend.agents.monitoring_agent import MonitoringAgent
from backend.agents.solutions_expert import SolutionsExpert


class ExperimentWorkflow:
    def __init__(self):
        self.planner = ExperimentPlanner()
        self.monitor = MonitoringAgent()
        self.solutions = SolutionsExpert()

    def propose(self, symptom: str) -> dict:
        return self.planner.propose(symptom)

    def diagnose(
        self,
        baseline: dict,
        current: dict,
    ) -> dict:
        monitoring_result = self.monitor.analyze(
            baseline, current
        )

        observations = monitoring_result[
            "analysis"
        ]["observations"]

        recommendation = self.solutions.recommend(
            observations
        )

        return {
            "monitoring": monitoring_result,
            "recommendation": recommendation,
        }
