from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_summary_http_200():
    response = client.get("/summary")
    assert response.status_code == 200


def test_get_summary_fields():
    response = client.get("/summary")
    data = response.json()
    assert "app" in data
    assert "version" in data
    assert "endpoints" in data
    assert "uptime_note" in data


def test_get_summary_values():
    response = client.get("/summary")
    data = response.json()
    assert data["app"] == "lobster-skills-test"
    assert data["version"] == "v1.0.0"
    assert isinstance(data["endpoints"], list)
    assert data["uptime_note"] == "service is running"


def test_get_ui_http_200():
    response = client.get("/ui")
    assert response.status_code == 200


def test_get_ui_content_type():
    response = client.get("/ui")
    assert "text/html" in response.headers["content-type"]
