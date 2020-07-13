# LRU Cache

Package for tracking store in-data memory using replacement cache algorithm / LRU cache. The Priority of storing or removing the data based on Min-Max heap algorithm or basic priority queue instead using OrderedDict module that provided by Python.

## Purpose

The purpose of using this package itself is at least to be able to dynamically tracking. inserting, and removing least frequently used in-data memory or in an element. Another purposes, with the use of python decorator or the method looks like, it's also possible to figure it out whether the data in the cache is full or not (it's called **LRU eviction**), since Min-Max heap algorithm is using *O(1)* complexity for basic insertion and searching, it's also possible to efficiently accessing the store in-data memory based on most frequently used method.

## Usage

LRUCache only works in Python version 3.5 and above, you can install it with :

```sh
pip install lrucache
```

There is a little explanation regarding the use of this LRU cache. The basic usage is pretty common by using a *List* and accessing that *List* like example :


```python
from lru.lrucache import LRUCache

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

The `get_dict()` method returns a dictionary of an object with a maximum capacity of 3 (which was initialized at first), whereas the objects that taken from the dictionary based on objects that are recently used (this is indicated by the `get()` method), while the `get_lru_element()` method is used for retrieve an object based on the duration when accessing onto the dictionary.

For further example, hopefully this package can be backported with Python web frameworks such as Django or Flask which can be implemented and supported in the JSON field area, since the return of this LRUCache value is in the form of dictionary which is very common in JSON type. For simple usage in Django, you must setting the LRUCache in installed application within Django settings like this :

```python

INSTALLED_APPS = [
    ...
    'lru',
    ...
]
```

And then you can create some function for wrapped the objects that you want to cached with `JsonResponse` from Django API. The results of this function will return your objects in the form of a JSON dict at your web browser :

```python
# views.py

from django.http import JsonResponse
from lru.lrucache import LRUCache

# set the capacity of LRUCache
test = LRUCache(3)

# wrapped our object
def test_lru(request):
    test.set(1, "foo")
    test.set(2, "bar")
    return JsonResponse(test.get_dict(), safe=False)
```

Dont forget to passing our function method into Django urls parameters :

```python
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_lru),
]
```

After that you can run the django server and see it in a web browser based on your endpoint url. **Please remember**, at the moment, each time after you wrapped the object with `JsonResponse`, you need to set the `safe` parameter to `False` because when you set an object with LRUCache, we don't set it to dict type, while the output from `JsonResponse` itself is dict type.

Likewise, the use of LRUcache in Django itself is very limited at this time, because there is a contradiction that is we can't set the objects dynamically, and another obstacle is that if the object that we set is not in the dict type, we need to do the object hashing. Normally, using LRUCache at the web-environment level can be done with the following assumptions like :

- You want to build web-based streaming services
- You do object modeling in the database, such as creating objects for a song that is least or most recently heard.
- You set the song object with LRUCache, so that every time you open your site, that song will appear.

Another example of using this LRU cache is that you want to display a book that is most often searched by keywords, dynamically remove an object that is not or least used, store data of users who frequently visit our site and many others.

## Why using this, instead of X?

Why use object cache level instead of filtering method or get method based on API? Ideally, cache is fast. and just fast as storage, reading or accessing the data from a cache takes less time than reading the data from something else. in example if you use filtering methods, you are doing accessing and getting the object from your database. Otherwise, caching the object improves performance by keeping recent or most used data in memory locations rather we're going to use computationally object from database.

## Roadmap

- [ ] Use classes as decorators for caching the objects
- [ ] Add expired time for caching objects
- [ ] Add thread safe parameter
- [ ] Scale the LRUCache capacity
- [ ] Backported and integrated with Django request and response


## Contributions

Since this package is still being under developed, any contributions are much welcomed and you can read on contribution page.

## License

This package is licensed under the MIT License.
