"""
LRUCache module for bypass thread safe in LRU.
"""


class BypassThreadSafe:
    """
    Classes for bypassing thread safe
    in LRU Cache class.
    """

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_tb):
        pass


def generate_hash_key(*args, **kwargs) -> int:
    """
    Helper function to generate a stable integer hash key
    from the given function arguments. Otherwise, when performed
    the cache lookup, passing arguments causing inconsistency
    hashing
    """
    return hash((args, tuple(sorted(kwargs.items()))))
