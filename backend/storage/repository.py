
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.storage.models import ExperimentRecord, FindingRecord


def create_experiment(
    db: Session,
    *,
    scenario: str,
    target_service: str,
    duration_seconds: int,
    rationale: str,
    result: dict,
    status: str = "completed",
    simulation_mode: bool = True,
) -> ExperimentRecord:
    record = ExperimentRecord(
        scenario=scenario,
        target_service=target_service,
        duration_seconds=duration_seconds,
        rationale=rationale,
        result=result,
        status=status,
        simulation_mode=simulation_mode,
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def get_experiment(
    db: Session, experiment_id: int
) -> ExperimentRecord | None:
    return db.get(ExperimentRecord, experiment_id)


def list_experiments(
    db: Session, limit: int = 50
) -> list[ExperimentRecord]:
    statement = (
        select(ExperimentRecord)
        .order_by(ExperimentRecord.id.desc())
        .limit(limit)
    )
    return list(db.scalars(statement).all())


def create_finding(
    db: Session,
    *,
    title: str,
    severity: str,
    evidence: str,
    recommendation: str,
    experiment_id: int | None = None,
) -> FindingRecord:
    record = FindingRecord(
        title=title,
        severity=severity,
        evidence=evidence,
        recommendation=recommendation,
        experiment_id=experiment_id,
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def list_findings(
    db: Session, limit: int = 50
) -> list[FindingRecord]:
    statement = (
        select(FindingRecord)
        .order_by(FindingRecord.id.desc())
        .limit(limit)
    )
    return list(db.scalars(statement).all())
