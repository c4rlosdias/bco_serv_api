from fastapi import APIRouter
from api.v1.endpoints import composicao

api_router = APIRouter()
api_router.include_router(composicao.router, prefix='/composicoes', tags=['composicoes'])

