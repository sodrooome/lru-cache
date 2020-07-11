import time
from heap import Heap # noqa

class LRUCache:

    def __init__(self, capacity: int=128):
        """Constructor for LRU Cache objects."""
        self.capacity = capacity
        self.dict = {}
        self.cache = Heap()

    def get_cache(self, key: int):
        if self.dict.get(key):
            return True
        return False

    def get_capacity(self):
        if len(self.dict) > self.capacity:
            return True
        return False

    def set(self, key: int, value: int) -> int:
        access_time = time.time()

        if self.get_cache(key):
            # update method is not working
            # should write update() method
            # in heap module
            self.cache.update(key, access_time)
            self.cache[key] = (value, access_time)
            return self.cache

        if self.get_capacity():
            minimum = self.cache.remove()[0]
            del self.dict[minimum]

        self.cache.add(key, access_time)
        self.dict[key] = (value, access_time)
        return self.dict

    def get(self, key: int):
        if not self.get_cache(key):
            raise KeyError("Cache key not in elements.")

        access_time = time.time()
        self.cache.update(key, access_time)
        value = self.dict[key][0]
        self.dict[key] = (value, access_time)
        return value

    def get_lru_element(self):
        key = self.cache.heap[0][1]
        return self.dict[key]

    def get_dict(self):
        return self.dict

# mock test
test = LRUCache(3)

test.set(1, "test")
test.set(2, "foo")
test.set(3, "fc")

test.get(1)
print(test.get_dict())