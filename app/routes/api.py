"""
Define API routes.
"""
import flask

from ..controllers.api import status


def configure(router: flask.Blueprint) -> flask.Blueprint:
    """Configure API routes."""

    router.route('/status', methods={'GET'})(status)

    return router
