import functools
from lru.lrucache import LRUCache
from datetime import datetime, timedelta
from typing import Any


def lru_cache(capacity: int = 128, **kwargs) -> Any:
    """Decorators for LRUCache classes. Given the
    capacity of cache based on LRUCache classes, for example:

    ```
    @lru_cache(capacity=3)
    def foo(x):
        pass
    """
    def wrapper():
        return LRUCache(capacity=capacity, **kwargs)
    return wrapper


def lru_cache_time(capacity: int = 128, seconds: int = 60*15, **kwargs) -> int:
    """Decorators for LRUCache classes using
    expired cached time. This is an mock only,
    probably not ready to bump into major version. for example:

    ```
    @lru_cache_time(capacity=3, seconds=60)
    def foo(x):
        pass
    ```
    """
    def wrapper(func):
        update_time = timedelta(seconds=seconds)
        next_update_time = datetime.utcnow() + update_time
        now_time = datetime.utcnow()
        func = LRUCache(capacity=capacity, seconds=seconds, **kwargs)
        return func

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            # using nonlocal for defined
            # variable inside nested function
            nonlocal next_update_time, func
            if now_time > next_update_time:
                func.clear_all()
                next_update_time = now_time + update_time
            return func(*args, **kwargs)
        return wrapped
    return wrapper
