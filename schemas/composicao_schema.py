from typing import Optional
from pydantic import BaseModel as SCBaseModel

class ComposicaoSchema(SCBaseModel):
    id: Optional[int]
    cod_servico: str 
    cod_composicao: str 
    cod_eap: str 
    banco: str 
    descricao: str 
    unidade: str 
    validado_proj: bool 
    
    class Config:
        orm_mode = True