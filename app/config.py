import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "safe_default")
    DATABASE_URL = os.environ.get("DATABASE_URL", "safe_default")
