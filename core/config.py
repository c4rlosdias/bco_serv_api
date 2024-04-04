from typing import List
from pydantic import AnyHttpUrl, BaseConfig
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseConfig):
    API_V1_STR: str = 'api/v1'
    DB_URL: str = "postgresql+asyncpg://itc:teste@localhost:5432/composicoes"
    DBBaseModel = declarative_base()

    class Config:
        case_Sensitive = True


settings = Settings()
