from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_status_http_200():
    response = client.get("/status")
    assert response.status_code == 200


def test_get_status_fields():
    response = client.get("/status")
    data = response.json()
    assert data["status"] == "ok"
    assert data["agent"] == "lobster"
    assert "timestamp" in data


def test_get_status_timestamp_is_iso():
    from datetime import datetime
    response = client.get("/status")
    ts = response.json()["timestamp"]
    # 能解析即代表格式正確
    datetime.fromisoformat(ts)
