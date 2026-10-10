def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "running"
    assert payload["docs"] == "/docs"


def test_health_endpoint(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "healthy"
    assert payload["service"] == "bosch-backend"
    assert "timestamp" in payload


def test_topology_endpoint(client):
    response = client.get("/api/v1/topology")
    assert response.status_code == 200
    payload = response.json()
    assert payload["services"]
    assert payload["dependencies"]
    service_ids = {service["id"] for service in payload["services"]}
    for dependency in payload["dependencies"]:
        assert dependency["source"] in service_ids
        assert dependency["target"] in service_ids


def test_metrics_catalog_endpoint(client):
    response = client.get("/api/v1/metrics")
    assert response.status_code == 200
    assert "targets_up" in response.json()["available_metrics"]


def test_planner_endpoint(client):
    response = client.post(
        "/api/v1/planner/propose",
        json={"symptom": "Checkout is slow because payment is delayed"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["scenario"] == "dependency_delay"
    assert payload["target_service"] == "payment-mock"
    assert payload["mode"] == "simulation"


def test_planner_rejects_short_symptom(client):
    response = client.post(
        "/api/v1/planner/propose",
        json={"symptom": "x"},
    )
    assert response.status_code == 422
