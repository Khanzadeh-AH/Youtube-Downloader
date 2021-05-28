from fastapi import APIRouter, Query
from fastapi.templating import Jinja2Templates
from pytube import YouTube, Playlist
from starlette.requests import Request

templates = Jinja2Templates('app/templates')

router = APIRouter()


@router.get('/singlestreams/')
async def stream(request: Request, link: str = Query(...)):
    yt = YouTube(link)
    str_streams = [str(stream_element) for stream_element in yt.streams]
    return templates.TemplateResponse("streaminfo.html", {"request": request, "streams": str_streams})


@router.get('/playliststreams/')
async def stream(request: Request, link: str = Query(...)):
    yt = Playlist(link)
    first_video = yt.videos[0]
    str_streams = [str(stream_element) for stream_element in first_video.streams]
    return templates.TemplateResponse("streaminfo.html", {"request": request, "streams": str_streams})
