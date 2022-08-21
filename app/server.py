"""
Server
"""

import waitress

from .app import create_app
from .logger import get_logger, start_logger
from . import config


def run():
    """Run the app."""
    logger = get_logger("waitress")
    logger.setLevel(config.LOG_LEVEL)
    start_logger()

    app = create_app()
    waitress.serve(app, host=config.APP_HOST, port=config.APP_PORT)


def watch():
    """Watch files"""

    import hupper  # pylint: disable=import-outside-toplevel

    logger = get_logger("hupper")
    logger.setLevel(config.LOG_LEVEL)
    start_logger()

    reloader = hupper.start_reloader("app.server.run", logger=logger, verbose=2)
    reloader.watch_files(["app/**/*.py"])


if __name__ == "__main__":

    if config.DEBUG:
        watch()
    else:
        run()
