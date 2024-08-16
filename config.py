import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = True

DB_PATH = os.getenv("DB_PATH") or ""


JWT_KEY = os.getenv("JWT_KEY")