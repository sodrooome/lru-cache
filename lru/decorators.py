from lru.heap import Heap
from lru.lrucache import LRUCache

def lru_cache(capacity: int=128, **kwargs) -> int:
    """Decorators for LRUCache classes. Given the
    capacity of cache based on LRUCache classes, for example:
    
    ```
    @lru_cache(capacity=3)
    def foo(x):
        pass
    """
    def wrapper(func):
        return LRUCache(capacity=capacity, **kwargs)
    return wrapper


# mock test
"""
@lru_cache(capacity=5)
def test_lru(x):
    print("Calling f(" + str(x) + ")")
    return x

test_lru.set(1, "foo")
test_lru.set(2, "test")
test_lru.set(3, "foos")
test_lru.set(4, "fc")
test_lru.set(5, "set")
print(test_lru.get_capacity())
"""