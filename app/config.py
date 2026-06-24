import os

class Config:
    SECRET_KEY = os.environ["SECRET_KEY"]       # KeyError when empty
    DATABASE_URL = os.environ["DATABASE_URL"]   # localhost unreachable in CI
