from fastapi.testclient import TestClient

from app.views.downloadinfo import router

client = TestClient(router)


def test_single_download():
    pass


def test_playlist_download():
    pass
