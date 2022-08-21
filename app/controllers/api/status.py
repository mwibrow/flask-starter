"""
Status controller.
"""
from flask import jsonify, Response

from ...config import PKG_NAME, PKG_VERSION


def status() -> Response:
    """Return status of the app."""
    return jsonify(dict(
        name=PKG_NAME,
        version=PKG_VERSION,
        status='healthy'
    ))
