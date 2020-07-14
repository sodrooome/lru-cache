import time
from lru.heap import Heap
from abc import ABC, abstractmethod, ABCMeta

class BoundedLRUCache:

    __metaclass__ = ABCMeta

    @abstractmethod
    def clear_all(self):
        """Remove all element in cache dict."""

class LRUCache(BoundedLRUCache):

    def __init__(self, capacity: int=128):
        """Constructor for LRU Cache objects."""
        self.capacity = capacity
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
        value = self.dict[key][0]
        self.dict[key] = (value, access_time)
        return value

    def get_lru_element(self):
        """Returned a dict type based on their key in cache element."""
        key = self.cache.heap[0][1]
        return self.dict[key]

    def get_dict(self):
        """Returned a dict type in cache element."""
        return self.dict

# mock test
test = LRUCache()

test.set(1, "test")
test.set(2, "foo")
test.set(3, "fc")
print(test.get_dict())
print(test.get_capacity())
print(test.get_cache(5))
# print(test.clear_cache(1))
print(test.clear_all())
print(test.get_dict())