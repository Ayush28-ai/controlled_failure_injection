import { api } from "./client";

export type Scenario = "service_shutdown" | "dependency_delay" | "traffic_spike";
export type Experiment = {
  id: number; scenario: Scenario; target_service: string; status: string;
  simulation_mode: boolean; duration_seconds: number; rationale: string;
  result: Record<string, unknown>; created_at: string;
};
export type ExperimentInput = {
  scenario: Scenario; target_service: string; duration_seconds: number; rationale: string;
};
export const listExperiments = () => api<Experiment[]>("/experiments?limit=100");
export const getExperiment = (id: number) => api<Experiment>(`/experiments/${id}`);
export const createExperiment = (input: ExperimentInput) =>
  api<Experiment>("/experiments", { method: "POST", body: JSON.stringify(input) });
export const proposeExperiment = (symptom: string) =>
  api<Record<string, unknown>>("/planner/propose", { method: "POST", body: JSON.stringify({ symptom }) });
export const recoverExperiment = (id: number) =>
  api<Record<string, unknown>>(`/recovery/${id}`, { method: "POST" });
