from core.config import settings
from sqlalchemy import Column, Integer, String, Boolean

class ComposicaoModel(settings.DBBaseModel):
    __tablename__ = 'composicoes'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    cod_servico: str = Column(String(100))
    cod_composicao: str = Column(String(100))
    cod_eap: str = Column(String(100))
    banco: str = Column(String(100))
    descricao: str = Column(String(100))
    unidade: str = Column(String(10))
    validado_proj: bool = Column(Boolean)