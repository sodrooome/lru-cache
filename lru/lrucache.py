import time
import threading
from .heap import Heap
from .utils import BypassThreadSafe
from abc import ABCMeta, abstractmethod
from typing import Union, Any


class BoundedLRUCache(metaclass=ABCMeta):
    """Abstract base class for bounded LRU cache implementation"""

    @abstractmethod
    def clear_all(self) -> None:
        """Clear all cache in element"""
        pass  # pragma: no cover


class LRUCache(BoundedLRUCache):
    """
    Initial class for representing LRUCache, given the several parameter such as :

    :param capacity: param for set the cache capacity, maximum number is 128
    :param seconds: param for set the duration for store the cache, maximum is 15 minutes
    :param thread_safe: param for enable/disable thread safe option, default is False
    """

    def __init__(
        self, capacity: int = 128, seconds: int = 60 * 15, thread_safe: bool = False
    ) -> None:
        self.capacity = capacity
        self.seconds = seconds
        self._cache_dict = {}
        self.cache = Heap()
        self.lock = threading.RLock() if thread_safe else BypassThreadSafe()

        # merged at 0.1.4
        if not isinstance(capacity, int):
            raise ValueError("Expected to set the capacity of cache.")
        elif capacity > 128:
            raise ValueError("Maximum capacity of cache is 128.")
        elif capacity < 0:
            raise ValueError("Cache capacity can't set below zero.")

        if not isinstance(seconds, int):
            raise ValueError("Expected to set the duration of cache in seconds time.")
        elif seconds > 60 * 15:
            raise ValueError("Maximum duration of cache is 15 minutes.")
        elif seconds < 0:
            raise ValueError("Cache duration can't set below zero time.")

    def __call__(self, *args, **kwargs):
        return self.cache

    @property
    def __len__(self) -> int:
        """
        property for get length of the cache capacity
        """
        return len(self._cache_dict)

    def __str__(self) -> str:
        return "%s" % self._cache_dict

    def __eq__(self, other: object):
        """Compare two LRUCache objects for the hashing equality"""
        if not isinstance(other, object):
            return NotImplemented
        return self._cache_dict == other._cache_dict

    def __hash__(self) -> int:
        """Return hash of the LRUCache object and make it hashable"""
        # consider to use this if the cache dict is unhashable
        # some cases when this happens if the cache changes
        print("The hash for dict object is: ")
        return hash(frozenset(self._cache_dict.items()))

    @property
    def ttl(self) -> int:
        """
        property for get TTL (time-to-live) in seconds.
        """
        return self.seconds

    def is_empty(self) -> bool:
        """
        Check whether the cache element is empty or not,
        return `True` if is empty otherwise will
        return `False` if is not empty
        """
        if len(self._cache_dict) == 0:
            return True
        return False

    def clear_all(self) -> None:
        """
        Clear all cache in element
        """
        return self._cache_dict.clear()

    def clear_cache_key(self, key: int) -> None:
        """
        Clear cache in element based on their key.

        :param key: given key parameter as an integer to clear the cache
        """
        with self.lock:
            if self.get_cache(key):
                return self._cache_dict.clear()

    def get_duration(self, expired_time: int = 3600) -> bool:
        """
        Get duration of cache, return `True` if the duration
        is exceed for expired time otherwise return `False`
        when the duration is even or below the expired time.

        :param expired_time: given expired_time parameter as an integer in seconds
        """
        if expired_time >= self.seconds:
            return True
        return False

    def get_ttl(self, key: int) -> Union[int, bool]:
        """
        Get time-to-live an objects based on their
        cache keys. Return False if the objects hasn't a key
        or time-to-live is expired.

        :param key: given key parameter as an integer to fetch the TTL
        """

        # since the new version 1.1.0, always lock the thread safe
        with self.lock:
            if key not in self._cache_dict:
                return False

            _, access_time = self._cache_dict[key]
            elapsed_time = time.perf_counter() - access_time
            ttl = self.seconds - elapsed_time

            if ttl > 0:
                return int(ttl)
            else:
                return False

    def get_cache(self, key: int) -> bool:
        """
        Get cache in element based on their key, return
        `True` if the element has a key, otherwise return `False`
        when element hasn't a key.

        :param key: given key parameter as an integer to fetch the cache
        """
        with self.lock:
            if self._cache_dict.get(key):
                return True
            return False

    def get_capacity(self) -> bool:
        """
        Get cache capacity, return `True` if the cache
        is full otherwiser return `False` when the cache
        is not full.
        """
        if len(self._cache_dict) > self.capacity:
            return True
        return False

    def set(self, key: int, value: str) -> dict:
        """
        Set an objects that wants to be cached

        :param key: given key parameter as an integer
        :param value: given value parameter of that key as an string
        """
        access_time: float = time.perf_counter()

        # always lock the thread safe, otherwise
        # multiple threads can cause the corruption
        # in such case, race condition will happen
        with self.lock:
            if self.get_cache(key=key):
                self.cache.update(key, access_time)
                self._cache_dict[key] = (value, access_time)
                return self._cache_dict

            if self.get_capacity():
                minimum = self.cache.remove()[0]
                del self._cache_dict[minimum]

            self.cache.add(key, access_time)
            self._cache_dict[key] = (value, access_time)
            return self._cache_dict

    def get(self, key: int) -> Any:
        """
        Get the objects based on their key in cache element

        :param key: given key parameter as an integer
        """

        # always make sure to lock the thread safe
        with self.lock:
            if not self.get_cache(key):
                raise KeyError(f"Cache key is not found in the cache element")

            access_time: float = time.perf_counter()
            self.cache.update(key, access_time)
            value = self._cache_dict[key][0]
            self._cache_dict[key] = (value, access_time)
            return value

    def get_lru_element(self) -> Any:
        """
        Returned a least recently used element in cache element.
        """
        with self.lock:  # pragma: no cover
            key = self.cache.heap[0][0]
            return self._cache_dict[key]

    def get_dict(self) -> dict:
        """
        Returned a dict type in cache element.
        """
        return self._cache_dict
