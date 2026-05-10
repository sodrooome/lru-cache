"""
LRUCache module for Decorators
"""

import functools
from lru.lrucache import LRUCache
from datetime import datetime, timedelta
from typing import Any
from lru.utils import generate_hash_key


def lru_cache(capacity: int = 128, **kwargs) -> Any:
    """
    Decorators for LRUCache classes. Given the
    capacity of cache based on LRUCache classes

    Example: ::

        @lru_cache(capacity=3)
        def foo(x):
            pass

    """

    def wrapper(func):
        cache = LRUCache(capacity=capacity, **kwargs)

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            key = generate_hash_key(*args, **kwargs)

            if cache.get_cache(key):
                return cache.get(key)

            result = func(*args, **kwargs)
            cache.set(key, result)
            return result

        return wrapped

    return wrapper


def lru_cache_time(capacity: int = 128, seconds: int = 60 * 15, **kwargs) -> int:
    """
    Decorator that wraps a function with an LRUCache instance and a time-based
    expiry. The entire cache is cleared automatically once the TTL has elapsed,
    and the expiration window time resets from that point

    :param capacity (int): maximum number of entries to store in the cache queue
    :param seconds (int): cache TTL in seconds before cache clear is being triggered
    :param kwargs: additional keywords argument passed to the LRUCache

    Returns:
        Callabe: a decorator that wraps the target with time-based caching

    Example ::

        @lru_cache_time(capacity=3, seconds=180)
        def foo(x):
            return x * 2
    """

    def wrapper(func):
        update_time = timedelta(seconds=seconds)
        next_update_time = datetime.utcnow() + update_time
        cached = LRUCache(capacity=capacity, seconds=seconds, **kwargs)

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            # using nonlocal for defined
            # variable inside nested function
            nonlocal next_update_time

            # move the now_time inside wrapper
            # and would be evaluate fresh on every call
            # fixing old bug which is the time never advances
            # and will never return True
            now_time = datetime.utcnow()
            if now_time > next_update_time:
                cached.clear_all()
                next_update_time = now_time + update_time

            key = generate_hash_key(*args, **kwargs)

            if cached.get_cache(key):
                return cached.get(key)

            result = func(*args, **kwargs)
            cached.set(key, result)

            return result

        return wrapped

    return wrapper
