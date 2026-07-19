import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")
)

env_path = os.path.join(BASE_DIR, ".env")

print("ENV PATH =", env_path)

load_dotenv(env_path)

print("DATABASE_URL =", os.getenv("DATABASE_URL"))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = (
        os.getenv("DATABASE_URL")
        or "sqlite:///expense_tracker.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JWT_ACCESS_TOKEN_EXPIRES = 3600