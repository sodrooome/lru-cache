import time
import threading
import weakref
from lru.heap import Heap
from abc import ABC, abstractmethod, ABCMeta

class BoundedLRUCache:

    __metaclass__ = ABCMeta

    @abstractmethod
    def clear_all(self):
        """Remove all element in cache dict."""

class LRUCache(BoundedLRUCache):

    def __init__(self, capacity: int=128, seconds: int=60*15):
        """Constructor for LRU Cache objects. Given
        the several parameter such as:

        :capacity: param for set the cache capacity, maximum
        number is 128

        :seconds: param for set the duration for store the cache,
        maximum is 15 minutes
        
        :dict: param for set the key and value into dict type
        """
        self.capacity = capacity
        self.seconds = seconds
        self.dict = {}
        self.cache = Heap()

        if capacity is None:
            raise ValueError("Capacity must be set.")

    def __call__(self, *args, **kwargs):
        return self.cache

    def __len__(self):
        return len(self.capacity)

    def clear_all(self):
        return self.dict.clear()

    def clear_cache_key(self, key: int) -> int:
        """Clear cache in element based on their key."""
        return self.cache.remove_key(key)

    def get_duration(self, expired_time: int=3600) -> int:
        """Get duration of cache, return `True` if the duration
        is exceed for expired time otherwise return `False` 
        when the duration is even or below the expired time.
        """
        if expired_time >= self.seconds:
            return True
        return False

    def get_ttl(self, key: int) -> int:
        """Get time-to-live an objects based on their
        cache keys. Return False if the objects hasn't a key
        or time-to-live is expired.
        """
        if self.get_cache(key):
            ttl = self.seconds - self.get_cache(key)
            if self.get_cache(key) >= 0:
                # got an unexpected result
                return ttl
        return None

    def get_cache(self, key: int):
        """Get cache in element based on their key, return
        `True` if the element has a key, otherwise return `False`
        when element hasn't a key.
        """
        if self.dict.get(key):
            return True
        return False

    def get_capacity(self):
        """Get cache capacity, return `True` if the cache
        is full otherwiser return `False` when the cache
        is not full.
        """
        if len(self.dict) > self.capacity:
            return True
        return False

    def set(self, key: int, value: int) -> int:
        """Set an objects that wants to be cached.
        
        :key: given key parameter as an integer

        :value: given value parameter of that key as an integer
        """
        end = time.perf_counter()
        start = time.perf_counter()
        access_time = start - end

        if self.get_cache(key):
            # update method is not working
            # should write update() method
            # in heap module
            self.cache.update(key, access_time)
            self.dict[key] = (value, access_time)
            return self.dict

        if self.get_capacity():
            minimum = self.cache.remove()[0]
            del self.dict[minimum]

        self.cache.add(key, access_time)
        self.dict[key] = (value, access_time)
        return self.dict

    def get(self, key: int):
        """Get the objects based on their key in cache element

        :key: given key parameter as an integer
        """
        if not self.get_cache(key):
            raise KeyError("Cache key not in elements.")

        access_time = time.perf_counter()
        self.cache.update(key, access_time)
        value = self.dict.get(key)[0]
        self.dict[key] = (value, access_time)
        return value

    def get_lru_element(self):
        """Returned a dict type based on their key in cache element."""
        key = self.cache.heap[0][1]
        return self.dict[key]

    def get_dict(self):
        """Returned a dict type in cache element."""
        return self.dict

class ThreadSafe(LRUCache):
    """Inheritance classes from LRU Cache for enable
    thread safe parameter. Whenever this class is used
    for the cached object, the global environment will applies
    multi-threaded code and make sure that LRUCache method
    works properly.
    """
    def __init__(self, capacity: int=128, seconds: int=60*15, thread_safe=False):
        # super().__init__(capacity=capacity, seconds=seconds)
        self.capacity = capacity
        self.seconds = seconds
        self.thread_safe = thread_safe
        self.dict = Heap()

        if thread_safe:
            thread_safe = self.EmptyCache(threading.Thread)
            thread_safe.start()

    class EmptyCache(threading.Thread):
        # thread same as the daemon
        thread = True

        def __init__(self, cache: int, duration: int=60):
            # thread must be terminate
            # if thread not terminat, 
            # it will be looping over again
            # for right now using this method
            # to terminate thread
            def kill_self(self):
                del self

            self.cache_reference = weakref.ref(cache)
            self.duration = duration
            super(ThreadSafe.EmptyCache, self).__init__()

        def start_thread_safe(self):
            while self.cache_reference():
                _get_cache = self.cache_reference
                if _get_cache:
                    next_cache_expired = _get_cache.cleanup()
                    if next_cache_expired is None:
                        time.sleep(self.duration)
                    else:
                        time.sleep(next_cache_expired + 1)
                _get_cache = None

# mock test
"""
test = LRUCache(128, 60, False)

test.set(1, "value")
test.get(1)

# print(test.get_ttl(1))
# print(test.clear_cache(1))
# print(test.clear_all())
# print(test.get_dict())
"""