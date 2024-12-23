from pydantic import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "FinancialApp"
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite:///./financial_app.db"
    TIINGO_API_KEY: str = os.getenv("TIINGO_API_KEY")
    
    class Config:
        env_file = ".env"

settings = Settings()

# Validate API key
if not settings.TIINGO_API_KEY:
    raise ValueError("TIINGO_API_KEY must be set in environment variables")