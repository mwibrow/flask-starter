"""
Logger which logs JSON to stdout.
"""
import json
import logging
from logging import Logger, LoggerAdapter
import sys
from collections import OrderedDict
from typing import Dict, Union


from boltons import tbutils
from pythonjsonlogger import jsonlogger


class GCPFormatter(jsonlogger.JsonFormatter):
    """
    Format a log message into a usable format for Google Cloud Platform.
    """

    key_map = {"asctime": "timestamp", "levelname": "severity"}

    def process_log_record(self, log_record):
        """
        Rename some keys to make them compatible with GCP.

        Overridden from {jsonlogger.JsonFormatter.process_log_record}.
        """
        new_log_record = OrderedDict()
        for key, value in log_record.items():
            key = self.key_map.get(key, key)
            new_log_record[key] = value
        if "exc_info" in new_log_record:
            try:
                new_log_record["err"] = dict(
                    stack=json.loads(new_log_record["exc_info"])
                )
            except json.JSONDecodeError:
                new_log_record["err"] = dict(stack=new_log_record["exc_info"])

            del new_log_record["exc_info"]
        return new_log_record

    def formatException(self, ei) -> str:  # noqa
        """Format exceptions as a json"""
        try:
            return json.dumps(tbutils.ExceptionInfo.from_exc_info(*ei).to_dict())
        except ValueError:
            # Raised by `boltons.tbutils`
            return ""


def start_logger(level=None):
    """
    Start logging to stdout.
    """
    root = logging.getLogger()
    clear_handlers()
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(GCPFormatter("%(asctime) %(name) %(levelname) %(message)"))
    root.addHandler(handler)
    root.setLevel(level=level or logging.DEBUG)


def clear_handlers(name=None):
    """Clear log handlers."""
    log = logging.getLogger(name)
    try:
        while log.hasHandlers():
            log.handlers.pop()
    except IndexError:
        pass


def get_logger(name, extra: Dict = None) -> Union[Logger, LoggerAdapter]:
    """
    Get a logger identified by a name.
    """
    log = logging.getLogger(name)
    clear_handlers(name)
    if extra:
        return logging.LoggerAdapter(log, extra)
    return log
