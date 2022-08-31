"""
Server
"""

import waitress

from .app import create_app
from .logger import get_logger, start_logger
from .config import Config


def run():
    """Run the app."""
    logger = get_logger("waitress")
    logger.setLevel(Config.LOG_LEVEL)
    start_logger()

    app = create_app()
    waitress.serve(app, host=Config.APP_HOST, port=Config.APP_PORT)


def watch():
    """Watch files"""

    import hupper  # pylint: disable=import-outside-toplevel

    logger = get_logger("hupper")
    logger.setLevel(Config.LOG_LEVEL)
    start_logger()

    reloader = hupper.start_reloader("app.server.run", logger=logger, verbose=2)
    reloader.watch_files(["app/**/*.py"])


if __name__ == "__main__":

    if Config.DEBUG:
        watch()
    else:
        run()
