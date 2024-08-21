from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from app.configuration.db_helper import db_helper
from app.core.crud.base import get_sentiment_by_phrase

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/sentiment_analise")
async def hf_sentiment_analise(
        phrase: str,
        session: AsyncSession = Depends(
            db_helper.scoped_session_dependency)):

    return await get_sentiment_by_phrase(session, phrase)
