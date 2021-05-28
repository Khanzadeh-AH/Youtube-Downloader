from fastapi import APIRouter, WebSocket, Query
from typing import Optional
from fastapi.templating import Jinja2Templates
from pytube import YouTube
from starlette.requests import Request

templates = Jinja2Templates('app/templates')

router = APIRouter()


@router.get('/streams/')
async def stream(request: Request, link: str = Query(...)):
    yt = YouTube(link)
    str_streams = [str(stream_element) for stream_element in yt.streams]
    return templates.TemplateResponse("streaminfo.html", {"request": request, "streams": str_streams})


@router.get('/download/')
async def dl(request: Request, link: str = Query(...), itag: int = Query(...)):
    yt = YouTube(link)
    dl_link = yt.streams.get_by_itag(itag).url
    return templates.TemplateResponse("downloadpage.html", {"request": request, "dl_link": dl_link})
