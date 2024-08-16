from fastapi import APIRouter, Form
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from dao import get_all_travels

templates = Jinja2Templates(directory="templates")

web_router = APIRouter(
    prefix="",
)


@web_router.get("/")
@web_router.post("/", include_in_schema=True)
def index(request: Request, query: str = Form(None)):
    context = {
        "request": request,
        "travels": get_all_travels(50, 0, query),
        "title": "Main page",
    }
    response = templates.TemplateResponse("index.html", context=context)
    return response
