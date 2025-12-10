from fastapi import APIRouter

from app.api.v1.links import api_v1_links_router
from app.config import settings


api_v1_router = APIRouter()

api_v1_router.include_router(api_v1_links_router, prefix=settings.API_V1_LINKS_STR, tags=["links"])
