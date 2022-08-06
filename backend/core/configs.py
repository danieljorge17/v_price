import os

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = os.getenv('DB_URI')
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()