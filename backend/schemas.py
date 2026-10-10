
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


Scenario = Literal[
    "service_shutdown",
    "dependency_delay",
    "traffic_spike",
]


class ExperimentCreate(BaseModel):
    scenario: Scenario
    target_service: str = Field(min_length=1, max_length=128)
    duration_seconds: int = Field(default=10, ge=1, le=30)
    rationale: str = Field(default="", max_length=500)


class ExperimentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    scenario: str
    target_service: str
    status: str
    simulation_mode: bool
    duration_seconds: int
    rationale: str
    result: dict
    created_at: datetime


class FindingCreate(BaseModel):
    experiment_id: int | None = None
    severity: Literal["info", "low", "medium", "high", "critical"]
    title: str = Field(min_length=1, max_length=200)
    evidence: str = Field(default="", max_length=4000)
    recommendation: str = Field(default="", max_length=4000)


class FindingOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    experiment_id: int | None
    severity: str
    title: str
    evidence: str
    recommendation: str
    created_at: datetime


class PlanRequest(BaseModel):
    symptom: str = Field(min_length=3, max_length=500)
