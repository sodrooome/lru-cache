import time
import threading
import warnings
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
        # introduced at v1.3.0: remove the print statement is being
        # invoked silently and possibly causing an unexpected result
        return hash(frozenset(self._cache_dict.items()))
    
    def __contains__(self, key: int) -> bool:
        # introduced at v1.3.0: replace the named of `get_cache()` with
        # the standard Python's protocol. The callers can now write
        # the idiomatic key in cache list rather than manually check the existence
        with self.lock:
            return key in self._cache_dict
        
    def _has_key(self, key: int) -> bool:
        # introduced at v1.3.0: internal helpers, shouldn't be invoked from public APIs
        # the old approach called `get_cache()` which has a function
        # to re-acquires the lock and also holds the locks, caused fragile
        # pattern and having a possibility cause the double-lock
        return key in self._cache_dict
    
    def _is_expired(self, key: int) -> bool:
        # introduced at v1.3.0: internal helpers, shouldn't be invoked from public APIs
        # returns `True` when the cache entry associated with key whereas
        # the expiration has lived longer than configured TTL. This function
        # used to be enforce expiration during read process
        _, access_time = self._cache_dict[key]
        return (time.perf_counter() - access_time) > self.seconds

    def _evict(self, key: int) -> None:
        # introduced at v1.3.0: internal helpers, shouldn't be invoked from public APIs
        # remove a single entry from both dictionaries and heap object
        del self._cache_dict[key]
        self.cache.remove_key(key=key)

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
        with self.lock:
            if len(self._cache_dict) == 0:
                return True
            return False

    def clear_all(self) -> None:
        """
        Clear all cache in element
        """
        with self.lock:
            self._cache_dict.clear()
            self.cache = Heap() # reset the heap to an empty state

    def clear_cache_key(self, key: int) -> None:
        """
        Clear cache in element based on their key.

        :param key: given key parameter as an integer to clear the cache
        """
        with self.lock:
            if self._has_key(key):
                self._evict(key)

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
            if not self._has_key(key):
                # since v1.3.0, lock free internal check
                return False

            _, access_time = self._cache_dict[key]
            elapsed_time = time.perf_counter() - access_time
            ttl = self.seconds - elapsed_time

            if ttl > 0:
                return int(ttl)
            
            # returned early eviction of the entry
            # while that entry already hold the lock
            self._evict(key=key)
            return False

    def get_cache(self, key: int) -> bool:
        """
        Get cache in element based on their key, return
        `True` if the element has a key, otherwise return `False`
        when element hasn't a key.

        :param key: given key parameter as an integer to fetch the cache
        """
        with self.lock:
            warnings.warn("This function has been deprecated since v1.3.0, you may use `get()` to get a cache objects")
            return key in self._cache_dict

    def get_capacity(self) -> bool:
        """
        Get cache capacity, return `True` if the cache
        is full otherwiser return `False` when the cache
        is not full.
        """
        if len(self._cache_dict) >= self.capacity:
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
            if not self._has_key(key):
                raise KeyError(f"Cache key is not found in the cache element")

            # fixed at v1.3.0: TTL is now being enforced on every read
            # which was already absent since initial release. Now,
            # expired entries are evicted as early as possible
            if self._is_expired(key=key):
                self._evict(key)
                raise KeyError(f"Cache key '{key}' has expired and evicted")
            
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
            # fixed at v1.3.0: added and empty guard which possibly
            # raises an IndexError if the cache was empty
            if not self.cache.heap:
                return None
            key = self.cache.heap[0][0]
            return self._cache_dict.get(key)

    def get_dict(self) -> dict:
        """
        Returned a dict type in cache element.
        """
        # introduced at v1.3.0: returning a shallow copy
        with self.lock:
            return dict(self._cache_dict)