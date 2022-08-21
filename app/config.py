"""
Configuration stuff.
"""
import logging
import os

env = os.environ.get

PKG_NAME = "flask-starter"
PKG_VERSION = "1.0.0"

APP_HOST = env("APP_HOST", "0.0.0.0")
APP_PORT = int(env("APP_PORT", "9100"))

API_VERSION = "v" + PKG_VERSION.split(".", maxsplit=1)[0]

DEBUG = env("PYTHON_ENV") == "development"

LOG_LEVEL = logging.getLevelName(env("LOG_LEVEL", logging.DEBUG))
