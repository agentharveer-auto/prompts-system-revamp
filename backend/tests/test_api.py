import pytest
from fastapi.testclient import TestClient
from backend.app.main import app, prompts_db

client = TestClient(app)


def test_create_prompt():
    payload = {"title": "Test Prompt", "content": "This is a test.", "owner": "tester"}
    resp = client.post("/prompts", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert "id" in data
    assert data["title"] == payload["title"]


def test_list_prompts():
    resp = client.get("/prompts")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)


def test_versions_workflow():
    # create a prompt first
    payload = {"title": "Versioned", "content": "content", "owner": "alice"}
    resp = client.post("/prompts", json=payload)
    pid = resp.json()["id"]
    # add a version
    ver_payload = {"author": "alice", "summary": "first edit"}
    resp2 = client.post(f"/prompts/{pid}/versions", json=ver_payload)
    assert resp2.status_code == 200
    ver = resp2.json()
    assert "version_id" in ver
    # fetch versions
    resp3 = client.get(f"/prompts/{pid}/versions")
    assert resp3.status_code == 200
    versions = resp3.json()
    assert isinstance(versions, list)
