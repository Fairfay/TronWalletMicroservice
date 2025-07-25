from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Конфигурация приложения с использованием Pydantic BaseSettings.
    Только необходимые поля для TronWalletMicroservice.
    """
    app_title: str = 'Tron Wallet Microservice'
    app_description: str = 'Microservice for Tron address info'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    postgres_user: str = 'admin'
    postgres_password: str = 'admin123'
    postgres_db: str = 'mydatabase'

    class Config:
        env_file = '.env'


settings = Settings()