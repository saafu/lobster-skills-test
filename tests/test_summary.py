from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_summary_http_200():
    response = client.get("/summary")
    assert response.status_code == 200


def test_get_summary_fields():
    response = client.get("/summary")
    data = response.json()
    assert "service" in data
    assert "version" in data
    assert "env" in data
    assert "routes" in data


def test_get_summary_values():
    response = client.get("/summary")
    data = response.json()
    assert data["service"] == "lobster-skills-test"
    assert data["version"] == "v1.0.0"
    assert data["env"] == "test"
    assert isinstance(data["routes"], list)


def test_get_ui_http_200():
    response = client.get("/ui")
    assert response.status_code == 200


def test_get_ui_content_type():
    response = client.get("/ui")
    assert "text/html" in response.headers["content-type"]
