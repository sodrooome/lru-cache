# LRU Cache

Package for tracking store in-data memory using replacement cache algorithm / LRU cache. The Priority of storing or removing the data based on Min-Max heap algorithm or basic priority queue instead using OrderedDict module that provided by Python.

## Purpose

The purpose of using this package itself is at least to be able to dynamically tracking. inserting, and removing least frequently used in-data memory or in an element. Another purposes, with the use of python decorator or the method looks like, it's also possible to figure it out whether the data in the cache is full or not (it's called **LRU eviction**), since LRU cache is using *O(1)* complexity, it's also possible to efficiently accessing the store in-data memory based on most frequently used method.

## Usage

The package is still being under developed and haven't packaged and published into PyPi index. However, there is a little explanation regarding the use of this LRU cache. The basic usage is pretty common by using a *List* and accessing that *List* like example :


```python
from lru import LRUCache

# set the max of cache capacity
foo = LRUCache(3)

# set the items
foo.set(1, "value")
foo.set(2, "cooke")
foo.set(3, "water")
foo.set(4, "gets")
foo.set(5, "sets")

# get the items
foo.get(3)
foo.get(4)
foo.get(5)

print(foo.get_dict())
print(foo.get_lru_element())
```

The `get_dict()` method returns a dictionary of an object with a maximum capacity of 3 (which was initialized at first), whereas the objects that taken from the dictionary based on objects that are most frequently used (this is indicated by the `get()` method), while the `get_lru_element()` method is used for retrieve an object based on the duration when accessing onto the dictionary.

For further example, hopefully this package can be backported with Python web frameworks such as Django or Flask which can be implemented and supported in the JSON field area, since the return of this LRUCache value is in the form of dictionary which is very common in JSON type.

## Contributions

Since this package is still being under developed, any contributions are much welcomed and you can read on contribution page.

## License

This package is licensed under the MIT License.
