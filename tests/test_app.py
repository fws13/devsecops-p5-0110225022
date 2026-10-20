import pytest
from app.main import create_app, service
from app.validators import validate_note
from app.utils import truncate


@pytest.fixture
def client():
    service._notes.clear()
    service._next_id = 1
    return create_app().test_client()


def test_validate_note_ok():
    assert validate_note({"title": "A", "content": "B"})[0] is True


def test_validate_note_empty_title():
    assert validate_note({"title": "", "content": "B"})[0] is False


def test_truncate():
    assert truncate("x" * 100, 10) == "xxxxxxxxxx..."


def test_create_and_get_note(client):
    r = client.post("/notes", json={"title": "Basis Data", "content": "Normalisasi"})
    assert r.status_code == 201
    assert client.get("/notes/1").get_json()["title"] == "Basis Data"


def test_create_invalid(client):
    assert client.post("/notes", json={"title": ""}).status_code == 400


def test_delete_note(client):
    client.post("/notes", json={"title": "T", "content": "C"})
    assert client.delete("/notes/1").status_code == 200
    assert client.get("/notes/1").status_code == 404
