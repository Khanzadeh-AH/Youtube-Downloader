from fastapi import APIRouter, Query
from fastapi.templating import Jinja2Templates
from pytube import YouTube, Playlist
from starlette.requests import Request

templates = Jinja2Templates('app/templates')

router = APIRouter()


@router.get('/singledownload/')
async def sddownload(request: Request, link: str = Query(...), itag: int = Query(...)):
    yt = YouTube(link)
    dl_link = yt.streams.get_by_itag(itag).url
    return templates.TemplateResponse("singledownloadpage.html", {"request": request, "dl_link": dl_link})


@router.get('/playlistdownload/')
async def pdownload(request: Request, link: str = Query(...), itag: int = Query(...)):
    yt = Playlist(link)
    download_links = []
    for video in yt.videos:
        download_links.append(video.streams.get_by_itag(itag).url)
    return templates.TemplateResponse("playlistdownloadpage.html", {"request": request, "dl_links": download_links})


@router.get('/singledownloadj/')
async def sddownloadj(link: str = Query(...), itag: int = Query(...)):
    yt = YouTube(link)
    dl_link = yt.streams.get_by_itag(itag).url
    return {"dl_link": dl_link}


@router.get('/playlistdownloadj/')
async def pdownload(link: str = Query(...), itag: int = Query(...)):
    yt = Playlist(link)
    download_links = []
    for video in yt.videos:
        download_links.append(video.streams.get_by_itag(itag).url)
    return {"dl_links": download_links}
