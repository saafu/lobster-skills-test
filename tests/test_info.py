from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_info_status():
    response = client.get("/info")
    assert response.status_code == 200


def test_get_info_body():
    response = client.get("/info")
    data = response.json()
    assert data["service"] == "lobster-skills-test"
    assert data["version"] == "v1.0.0"
    assert data["env"] == "test"
