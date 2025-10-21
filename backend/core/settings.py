import os
from pathlib import Path
from dotenv import load_dotenv
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY","unsafe-dev")
DEBUG = os.getenv("DEBUG","True")=="True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS","*").split(",")

INSTALLED_APPS = [
  "django.contrib.admin","django.contrib.auth","django.contrib.contenttypes",
  "django.contrib.sessions","django.contrib.messages","django.contrib.staticfiles",
  "rest_framework","corsheaders","core",
]
MIDDLEWARE = ["corsheaders.middleware.CorsMiddleware", *[
  "django.middleware.security.SecurityMiddleware","django.contrib.sessions.middleware.SessionMiddleware",
  "django.middleware.common.CommonMiddleware","django.middleware.csrf.CsrfViewMiddleware",
  "django.contrib.auth.middleware.AuthenticationMiddleware","django.contrib.messages.middleware.MessageMiddleware",
  "django.middleware.clickjacking.XFrameOptionsMiddleware",
]]

if os.getenv("DB_ENGINE")=="postgres":
    DATABASES={"default":{
      "ENGINE":"django.db.backends.postgresql",
      "NAME":os.getenv("DB_NAME"),
      "USER":os.getenv("DB_USER"),
      "PASSWORD":os.getenv("DB_PASSWORD"),
      "HOST":os.getenv("DB_HOST"),
      "PORT":os.getenv("DB_PORT","5432"),
      "OPTIONS":{"sslmode":"require"},
    }}
else:
    from pathlib import Path
    DATABASES={"default":{"ENGINE":"django.db.backends.sqlite3","NAME":BASE_DIR/"db.sqlite3"}}
