from fastapi.testclient import TestClient

from app.views.streaminfo import router

client = TestClient(router)


def test_single_stream():
    pass


def test_playlist_stream():
    pass
