"""
Configure application.
"""

import time
from uuid import uuid4

from flask import Blueprint, Flask, g, jsonify, request, Response
from flask.logging import create_logger
import werkzeug.exceptions

from app.logger import get_logger

from . import config
from .routes import api as api_routes


def create_app():
    """
    Configure application.
    """
    app = Flask(__name__)

    log = create_logger(app)

    @app.before_request
    def _():
        g.start = time.time()
        g.log = get_logger(log.name, {"requestId": uuid4()})

    @app.after_request
    def _(response: Response):
        duration = round((time.time() - g.start) * 1000, 3)
        extra = dict(
            duration=duration,
            method=request.method,
            path=request.path,
            status=response.status_code,
        )
        g.log.debug(
            "%s %s %s %s %sms - %s",
            request.method,
            request.url,
            response.status_code,
            len(response.data),
            duration,
            request.headers.get("User-Agent"),
            extra=extra,
        )
        return response

    api_router = Blueprint("api", "api", url_prefix=f"/api/{config.API_VERSION}")
    api_router = api_routes.configure(api_router)
    app.register_blueprint(api_router)

    @app.errorhandler(404)
    def _(error: werkzeug.exceptions.NotFound):
        return jsonify(dict(message="page not found", error=error.description))

    @app.errorhandler(500)
    def _(error: werkzeug.exceptions.InternalServerError):
        return jsonify(dict(message="internal server error", error=error.description))

    return app
