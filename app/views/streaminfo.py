from fastapi import APIRouter, WebSocket, Query
from fastapi.templating import Jinja2Templates
from pytube import YouTube

templates = Jinja2Templates('app/templates')

router = APIRouter()


@router.get('/streams/')
async def stream(link: str = Query(...)):
    yt = YouTube(link)
    str_streams = [str(stream_element) for stream_element in yt.streams]
    return {"streams": str_streams}


# async def progress_function():
#     return 1


# @router.get('/download/')
# async def dl(link: str = Query(...), itag: int = Query(...), path: str = Query(...)):
#     yt = YouTube(link, on_progress_callback=progress_function())
#     desired_stream = yt.streams.get_by_itag(itag)
#     desired_stream.download(path)
#     pass


# @router.websocket_route('/downloading')
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await progress_function()
#         await websocket.send_text(f"Message text was: {data}")
