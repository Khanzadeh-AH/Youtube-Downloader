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
async def dl(link: str = Query(...), itag: int = Query(...), path: Optional[str] = Query(None)):
    yt = YouTube(link)
    desired_stream = yt.streams.get_by_itag(itag)
    if path:
        desired_stream.download(path)
    else:
        desired_stream.download()
    return {"success"}

