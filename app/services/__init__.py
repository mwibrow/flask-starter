"""
Services module.
"""

from abc import ABC, abstractmethod


class Service(ABC):
    """Abstract class for services."""

    @abstractmethod
    def set_up(self):
        """Set up the service (e.g., open a database connection)."""
        pass

    @abstractmethod
    def tear_down(self):
        """Tear down the service (e.g., close a database connection)"""
        pass
