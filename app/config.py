"""
Configuration stuff.
"""

import logging
import os
from typing import final


env = os.environ.get


class Config:
    """Configuration class."""
    PKG_NAME: final[str] = "flask-starter"
    PKG_VERSION: final[str] = "1.0.0"

    APP_HOST: final[str] = env("APP_HOST", "0.0.0.0")
    APP_PORT: final[int] = int(env("APP_PORT", "9100"))

    API_VERSION: final[str]= "v" + PKG_VERSION.split(".", maxsplit=1)[0]

    DEBUG: final[bool] = env("PYTHON_ENV") == "development"

    LOG_LEVEL: final[int] = logging.getLevelName(env("LOG_LEVEL", logging.DEBUG))

