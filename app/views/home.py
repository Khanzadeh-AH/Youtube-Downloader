from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

templates = Jinja2Templates('templates')

router = APIRouter()


@router.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})





