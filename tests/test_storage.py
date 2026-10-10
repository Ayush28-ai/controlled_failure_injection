from backend.storage.repository import (
    create_experiment,
    create_finding,
    get_experiment,
    list_experiments,
    list_findings,
)


def test_experiment_repository_persists_record(db_session):
    record = create_experiment(
        db_session,
        scenario="dependency_delay",
        target_service="payment-mock",
        duration_seconds=5,
        rationale="test",
        result={"mode": "simulation", "action_executed": False},
    )

    assert record.id is not None
    loaded = get_experiment(db_session, record.id)
    assert loaded is not None
    assert loaded.result["mode"] == "simulation"
    assert len(list_experiments(db_session)) == 1


def test_finding_repository_persists_record(db_session):
    finding = create_finding(
        db_session,
        title="Checkout latency increased",
        severity="medium",
        evidence="Latency increased from baseline",
        recommendation="Inspect payment dependency metrics",
    )

    assert finding.id is not None
    records = list_findings(db_session)
    assert len(records) == 1
    assert records[0].title == "Checkout latency increased"
