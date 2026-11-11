
import os
import cloudinary
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from sqlalchemy.engine import URL

load_dotenv()


class Settings(BaseSettings):
    # Database Settings
    POSTGRES_USERNAME: str = os.getenv("POSTGRES_USERNAME", "")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "")
    DB_HOST: str = os.getenv("DB_HOST", "127.0.0.1")
    DB_PORT: int = int(os.getenv("DB_PORT", "5432"))
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "")
    DB_CONNECTION: str = os.getenv(
        "DB_CONNECTION", "postgresql+psycopg"
    )

    # Cloudinary Settings
    CLOUD_NAME: str = os.getenv("CLOUDINARY_CLOUD_NAME", "")
    API_KEY: str = os.getenv("CLOUDINARY_API_KEY", "")
    API_SECRET: str = os.getenv("CLOUDINARY_API_SECRET", "")

    # JWT Authentication Settings (Hardcoded directly)
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your_fallback_secret_key_here")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 10080  # 7 days (7 * 24 * 60)

    # Validate Cloudinary configuration
    def configure_cloudinary(self):
        if not all([self.CLOUD_NAME, self.API_KEY, self.API_SECRET]):
            raise RuntimeError(
                "Missing Cloudinary configuration in environment variables."
            )

        cloudinary.config(
            cloud_name=self.CLOUD_NAME,
            api_key=self.API_KEY,
            api_secret=self.API_SECRET,
            secure=True,
        )

    # Database URL
    @property
    def SQLALCHEMY_DATABASE_URL(self) -> URL:
        return URL.create(
            drivername=self.DB_CONNECTION,
            username=self.POSTGRES_USERNAME,
            password=self.POSTGRES_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            database=self.POSTGRES_DB,
        )


settings = Settings()
settings.configure_cloudinary()
