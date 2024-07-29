from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = 'PyTest Tutorial'
    admin_email: str
    env: str
    token: str
    description: str = 'This is the app description'
    
    model_config = SettingsConfigDict(env_file='.env')

@lru_cache
def get_settings():
    return Settings()

# Initialize settings
settings = get_settings()