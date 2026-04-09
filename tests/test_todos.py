from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_todo():
    response = client.post("/todos/", json={
        "title": "Test todo",
        "description": "Test description"
    })
    assert response.status_code == 201
    assert response.json()["title"] == "Test todo"

def test_get_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
