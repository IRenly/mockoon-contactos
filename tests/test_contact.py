from fastapi.testclient import TestClient
from src.main import app  # ajusta si tu archivo está en otro módulo

client = TestClient(app)

def test_create_contact_success(monkeypatch):
    def mock_post(url, json):
        class MockResponse:
            status_code = 200
            def json(self):
                return {"allowed": True}
        return MockResponse()

    monkeypatch.setattr("requests.post", mock_post)

    response = client.post("/create_contact", json={
        "name": "Juan Pérez",
        "email": "juan@mail.com",
        "phone": "1234567890"
    })

    assert response.status_code == 201
    assert response.json()["name"] == "Juan Pérez"
    assert response.json()["email"] == "juan@mail.com"
    assert response.json()["phone"] == "1234567890"


def test_create_contact_rejected(monkeypatch):
    def mock_post(url, json):
        class MockResponse:
            status_code = 200
            def json(self):
                return {"allowed": False}
        return MockResponse()

    monkeypatch.setattr("requests.post", mock_post)

    response = client.post("/create_contact", json={
        "name": "Carlos Malo",
        "email": "bloqueado@mail.com",
        "phone": "0000000000"
    })

    assert response.status_code == 400
    assert response.json() == {"detail": "Email no permitido"}