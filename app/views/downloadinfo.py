from fastapi import APIRouter, Query
from fastapi.templating import Jinja2Templates
from pytube import YouTube, Playlist
from starlette.requests import Request

templates = Jinja2Templates('app/templates')

router = APIRouter()


@router.get('/singledownload/')
async def dl(request: Request, link: str = Query(...), itag: int = Query(...)):
    yt = YouTube(link)
    dl_link = yt.streams.get_by_itag(itag).url
    return templates.TemplateResponse("downloadpage.html", {"request": request, "dl_link": dl_link})


@router.get('/playlistdownload/')
async def dl(request: Request, link: str = Query(...), itag: int = Query(...)):
    yt = Playlist(link)
    download_links = []
    for video in yt.videos:
        download_links.append(video.streams.get_by_itag(itag).url)
    return templates.TemplateResponse("downloadpage.html", {"request": request, "dl_links": download_links})
