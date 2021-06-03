from fastapi import APIRouter, Query
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from pytube import YouTube, Playlist

template = Jinja2Templates("app/templates")

router = APIRouter()


@router.get("/singlestream/")
async def sstream(request: Request, link: str = Query(...)):
    yt = YouTube(link)
    title = yt.title
    thumbnail = yt.thumbnail_url
    stream_list = [stream for stream in yt.streams]

    return template.TemplateResponse("singlestreampage.html",
                                     {"request": request,
                                      "title": title,
                                      "thumbnail": thumbnail,
                                      "stream_list": stream_list})


@router.get("/playliststream/")
async def pstream(request: Request, link: str = Query(...)):
    pl = Playlist(link)
    video_dict = {}
    for video in pl.videos:
        video_dict[video.title] = [stream for stream in video.streams]
    return template.TemplateResponse("playliststreampage.html", {"request": request, "video_dict": video_dict})


@router.get("/singlestreamj/")
async def sstream(link: str = Query(...)):
    yt = YouTube(link)
    title = yt.title
    thumbnail = yt.thumbnail_url
    stream_list = [stream for stream in yt.streams]

    return {"title": title, "thumbnail": thumbnail, "stream_list": stream_list}


@router.get("/playliststreamj/")
async def pstream(link: str = Query(...)):
    pl = Playlist(link)
    video_dict = {}
    for video in pl.videos:
        video_dict[video.title] = [stream for stream in video.streams]
    return {"video_dict": video_dict}
