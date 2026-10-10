import { api } from "./client";
export type MetricSummary = { available_metrics: string[] };
export const listMetricNames = () => api<MetricSummary>("/metrics");
export const getMetric = (name: string) =>
  api<{ metric: string; data: { result?: Array<{ metric: Record<string, string>; value?: [number, string] }> } }>(`/metrics/${encodeURIComponent(name)}`);
export const getHealth = () => api<{ status: string; service: string; timestamp: string }>("/health");
export const getTopology = () => api<{ services: Array<{ id: string; name: string; type: string }>; dependencies: Array<{ source: string; target: string }> }>("/topology");
