from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.composicao_model import ComposicaoModel
from schemas.composicao_schema import ComposicaoSchema
from core.deps import get_session

router = APIRouter()

#POST composicao
@router.post('/', status_code = status.HTTP_201_CREATED, response_model=ComposicaoSchema)
async def post_composicao(composicao: ComposicaoSchema, db: AsyncSession = Depends(get_session)):
    nova_composicao = ComposicaoModel(cod_Servico = composicao.cod_servico,
                                      cod_composicao = composicao.cod_composicao,
                                      cod_eap = composicao.cod_eap,
                                      banco = composicao.banco,
                                      descricao = composicao.descricao,
                                      unidade = composicao.unidade,
                                      validado_proj = composicao.validado_proj  
    )
    db.add(nova_composicao)
    await db.commit
    return nova_composicao

#GET composicoes
@router.get('/', response_model=List[ComposicaoSchema])
async def get_composicoes(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ComposicaoModel)
        result = await session.execute(query)
        composicoes: List[ComposicaoModel] = result.scalars().all()

        return composicoes

#GET curso
@router.get('/{composicao_id}', response_model=ComposicaoSchema, status_code=status.HTTP_200_OK )
async def get_composicao(composicao_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ComposicaoModel).filter(ComposicaoModel.id == composicao_id)
        result = await session.execute(query)
        composicao = result.scalar_one_none()

        if composicao:
            return composicao
        else:
            raise HTTPException(detail='Composicao nao encontrada',
                                status_code=status.HTTP_404_NOT_FOUND)

# PUT composicao
@router.put('/{composicao_id}', response_model=ComposicaoSchema, status_code=status.HTTP_202_ACCEPTED )
async def put_composicao(composicao_id: int, composicao: ComposicaoSchema,  db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ComposicaoModel).filter(ComposicaoModel.id == composicao_id)
        result = await session.execute(query)
        composicao_up = result.scalar_one_none()

        if composicao_up:
            composicao_up.cod_Servico = composicao.cod_servico,
            composicao_up.cod_composicao = composicao.cod_composicao,
            composicao_up.cod_eap = composicao.cod_eap,
            composicao_up.banco = composicao.banco,
            composicao_up.descricao = composicao.descricao,
            composicao_up.unidade = composicao.unidade,
            composicao_up.validado_proj = composicao.validado_proj
            
            await session.commit()
            return composicao_up
        else:
            raise HTTPException(detail='Composicao nao encontrada',
                                status_code=status.HTTP_404_NOT_FOUND)

# DELETE composicao
@router.delete('/{composicao_id}', status_code=status.HTTP_204_NO_CONTENT )
async def delete_composicao(composicao_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ComposicaoModel).filter(ComposicaoModel.id == composicao_id)
        result = await session.execute(query)
        composicao_del = result.scalar_one_none()

        if composicao_del:
            await session.delete(composicao_del)            
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Composicao nao encontrada',
                                status_code=status.HTTP_404_NOT_FOUND