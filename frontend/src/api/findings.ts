import { api } from "./client";
export type Finding = {
  id: number; experiment_id: number | null; severity: "info" | "low" | "medium" | "high" | "critical";
  title: string; evidence: string; recommendation: string; created_at: string;
};
export const listFindings = () => api<Finding[]>("/findings?limit=100");
export const createFinding = (finding: Omit<Finding, "id" | "created_at">) =>
  api<Finding>("/findings", { method: "POST", body: JSON.stringify(finding) });
