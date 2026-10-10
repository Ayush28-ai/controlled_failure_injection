
from datetime import datetime, timezone

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    JSON,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column

from backend.storage.database import Base


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class ExperimentRecord(Base):
    __tablename__ = "experiments"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )
    scenario: Mapped[str] = mapped_column(String(64), index=True)
    target_service: Mapped[str] = mapped_column(String(128))
    status: Mapped[str] = mapped_column(
        String(32), default="queued", index=True
    )
    simulation_mode: Mapped[bool] = mapped_column(
        Boolean, default=True
    )
    duration_seconds: Mapped[int] = mapped_column(
        Integer, default=10
    )
    rationale: Mapped[str] = mapped_column(Text, default="")
    result: Mapped[dict] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utcnow
    )


class FindingRecord(Base):
    __tablename__ = "findings"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )
    experiment_id: Mapped[int | None] = mapped_column(
        ForeignKey("experiments.id"),
        nullable=True,
        index=True,
    )
    severity: Mapped[str] = mapped_column(
        String(16), default="info"
    )
    title: Mapped[str] = mapped_column(String(200))
    evidence: Mapped[str] = mapped_column(Text, default="")
    recommendation: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utcnow
    )
