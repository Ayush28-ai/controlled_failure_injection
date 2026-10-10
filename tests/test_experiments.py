def test_create_simulated_experiment_and_list_it(client):
    response = client.post(
        "/api/v1/experiments",
        json={
            "scenario": "dependency_delay",
            "target_service": "payment-mock",
            "duration_seconds": 5,
            "rationale": "Test checkout resilience",
        },
    )
    assert response.status_code == 201
    created = response.json()
    assert created["id"] > 0
    assert created["scenario"] == "dependency_delay"
    assert created["target_service"] == "payment-mock"
    assert created["status"] == "completed"
    assert created["simulation_mode"] is True
    assert created["result"]["mode"] == "simulation"
    assert created["result"]["action_executed"] is False

    listing = client.get("/api/v1/experiments")
    assert listing.status_code == 200
    assert any(item["id"] == created["id"] for item in listing.json())


def test_get_experiment_by_id(client):
    created = client.post(
        "/api/v1/experiments",
        json={
            "scenario": "service_shutdown",
            "target_service": "store-api",
            "duration_seconds": 3,
            "rationale": "Test API resilience",
        },
    ).json()

    response = client.get(f"/api/v1/experiments/{created['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == created["id"]


def test_unknown_experiment_returns_404(client):
    response = client.get("/api/v1/experiments/999999")
    assert response.status_code == 404


def test_unknown_scenario_rejected_by_schema(client):
    response = client.post(
        "/api/v1/experiments",
        json={
            "scenario": "unknown_scenario",
            "target_service": "store-api",
            "duration_seconds": 5,
            "rationale": "Invalid scenario",
        },
    )
    assert response.status_code == 422


def test_disallowed_target_is_rejected(client):
    response = client.post(
        "/api/v1/experiments",
        json={
            "scenario": "dependency_delay",
            "target_service": "untrusted-host",
            "duration_seconds": 5,
            "rationale": "Must be rejected",
        },
    )
    assert response.status_code == 422


def test_duration_over_limit_is_rejected(client):
    response = client.post(
        "/api/v1/experiments",
        json={
            "scenario": "dependency_delay",
            "target_service": "payment-mock",
            "duration_seconds": 31,
            "rationale": "Must be rejected",
        },
    )
    assert response.status_code == 422


def test_experiment_list_limit_validation(client):
    assert client.get("/api/v1/experiments?limit=0").status_code == 422
    assert client.get("/api/v1/experiments?limit=201").status_code == 422
