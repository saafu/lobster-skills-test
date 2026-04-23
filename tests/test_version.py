from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_version_http_200():
    response = client.get("/version")
    assert response.status_code == 200


def test_get_version_has_version_field():
    response = client.get("/version")
    data = response.json()
    assert "version" in data
    assert data["version"] == "1.0.0"


def test_get_version_has_env_field():
    response = client.get("/version")
    data = response.json()
    assert "env" in data
    assert data["env"] == "test"
