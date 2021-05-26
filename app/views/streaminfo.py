from fastapi import APIRouter, Query
from fastapi.templating import Jinja2Templates
from pytube import YouTube

templates = Jinja2Templates('templates')

router = APIRouter()


@router.get('/streams/')
async def stream(link: str = Query(...)):
    yt = YouTube(link)
    str_streams = [str(stream_element) for stream_element in yt.streams]
    return {"streams": str_streams}


@router.get('/download/')
async def dl(link: str = Query(...), itag: int = Query(...), path: str = Query(...)):
    yt = YouTube(link)
    desired_stream = yt.streams.get_by_itag(itag)
    desired_stream.download(path)
    pass
