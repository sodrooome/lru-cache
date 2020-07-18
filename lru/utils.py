"""Utils module for bypass thread safe in LRU."""

from collections import namedtuple

class BypassThreadSafe:
    """Classes for bypassing thread safe
    in LRU Cache class.
    """

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_tb):
        pass