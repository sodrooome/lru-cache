# LRU Cache

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/lruheap) ![PyPI - Status](https://img.shields.io/pypi/status/lruheap) ![PyPI](https://img.shields.io/pypi/v/lruheap) [![Downloads](https://pepy.tech/badge/lruheap)](https://pepy.tech/project/lruheap) [![Build Status](https://travis-ci.org/sodrooome/lru-cache.svg?branch=master)](https://travis-ci.org/sodrooome/lru-cache) [![Maintainability](https://api.codeclimate.com/v1/badges/9b20a52c48f76cc8d6ac/maintainability)](https://codeclimate.com/github/sodrooome/lru-cache/maintainability)

Package for tracking store in-data memory using replacement cache algorithm / LRU cache. The Priority of storing or removing the data based on Min-Max heap algorithm or basic priority queue instead using OrderedDict module that provided by Python.

## Purpose

The purpose of using this package itself is at least to be able to dynamically tracking. inserting, and removing least frequently used in-data memory or in an element. Another purposes, with the use of python decorator or the method looks like, it's also possible to figure it out whether the data in the cache is full or not (it's called **LRU eviction**), since Min-Max heap algorithm is using *O(1)* complexity for basic insertion and searching, it's also possible to efficiently accessing the store in-data memory based on most frequently used method.

## Usage

LRUCache only works in Python version 3.5 and above, you can install it with :

```sh
pip install lruheap
```

There is a little explanation regarding the use of this LRU cache. You can see at this simple configuration and explanation for using several method that provided by this package.

### `LRUCache(capacity=128, seconds=60*15)`

Class constructor for initialize LRUCache method with maximum capacity of cache is 128 and maximum duration of cache is 15 minutes when you don't initialize at first. For example:

```python
from lru.lrucache import LRUCache

foo = LRUCache(3)

# or you can set param argument
foo = LRUCache(capacity=3, seconds=5*15)
```

### `set()`

Set an objects that wants to be cached in cache element, given the `key` parameters and `value` parameters as integer. For example:

```python
foo.set(1, "foobar")
foo.set(2, "bar")
```

### `get()`

Get the objects based on their key in cache element and access time, given the `key` parameters as integer. This `get()` method can also be used to tracking which objects are often called which will later be identified as recently used objects in a cache element, an object that is often called by this method will be placed in front of the cache element by using `get_lru_element()`. For example:

```python
foo.get(1)
foo.get(1) # you can iterate for calling an object
foo.get(2)
```

### `get_dict()`

Method for returned a all dictionary of an object in cache element. For example:

```python
foo.get_dict()
```

### `get_duration()`

Method for getting duration of cache, return `True` if the duration is exceed for expired time otherwise return `False` when the duration is even or below the expired time. The expired time set as 3600 seconds. For example:

```python
# will return True if the duration
# of cache is still under the
# expired time
foo.get_duration()
```

### `get_lru_element()`

Method for retrieved an object based on their key in cache element and the duration when accessing onto the dictionary. 
If the object is not called by the `get()` method, then objects that have short time for accessing onto dictionary will be placed in beginning of the cache element, if the object is called by the `get()` method, it will placed depending how many objects are called. In this case, this called as recently used. For example:

```python
foo.get_lru_element()
```

### `get_capacity()`

Get cache capacity, return `True` if the cache is full otherwiser return `False` when the cache is not full. For example:

```python
foo.get_capacity()
```

### `get_cache()`

Get cache in element based on their key, return `True` if the element has a key, otherwise return `False` when element hasn't a key. Given the `key` parameters as integer. For example:

```python
foo.get_cache(1)
```

### `get_ttl()`

Get time-to-live (TTL) duration for cache, will return a value, where the value is the remaining time from the cache duration that has been set previously. Given the `key` parameters as integer. Th countdown time will be reduced by one second according to the cache duration that we have set before, if you set it to within 5 seconds, when using this method it will display a value of 4 which means its the remaining duration of our cache, and so on until the result displayed is set as`None`. For example:

```python
foo.get_ttl(1)
```

### `clear_all()`

Remove all cache in element. For example:

```python
foo.clear_all()
```

### `clear_cache_key()`

Remove cache in element based on their key. Given the `key` as parameters for remove the cache objects. For example:

```python
# this will remove cache
# object based on first index
foo.clear_cache_key(1)
```

### `is_empty()`

Check whether the current cache in element is empty or not. Will return `True` if the cache element is empty and `False` when the cache element is full of objects. For example:

```python
foo.is_empty()
```

### `@lru_cache(capacity=128)`

Python decorators using LRUCache classes for cache an object within a function. Default capacity is 128 if you not define it. For example:

```python
from lru.decorators import lru_cache

@lru_cache(capacity=5)
def test_lru(x):
    print("Calling f(" + str(x) + ")")
    return x

test_lru.set(1, "foo")
test_lru.set(2, "test")
test_lru.set(3, "foos")
test_lru.set(4, "fc")
test_lru.set(5, "set")
test_lru.get_capacity()
```

### `@lru_cache_time(capacity=128, seconds=60*15)`

Python decorators for LRUCache classes using expired cached time. This is an mock only, **probably** not ready to bump into major version, 
if you want to try it and there is an error or an unexpected result, please raise the issue. For example :

```python
from lru.decorators import lru_cache_time

@lru_cache_time(capacity=5, seconds=15)
def test_lru(x):
    print("Calling f(" + str(x) + ")")
    return x

test_lru.set(1, "foo")
test_lru.set(2, "test")
```

The difference between set duration of cache if using decorators or not lies when we set the value of the duration cache. By using these `@lru_cache_time` decorators at least it will compact and dynamically clear the cache if the duration exceeds of the maximum duration (15 minutes).

### Enable `thread_safe` parameter

By enabling `thread_safe` parameter into `True`, it will be possible to safely to call a function together. For example, if we create a shared task (functions a and b) where the shared task invokes a resource such as object from function c, then the object can safely be called and can be execute on both functions a and b (thus, its called a deadlock if we dont use `thread_safe` parameter to execute two functions from one resource). **As for concerns**, the use of `thread_safe` might be reduce the performance. For example:

```python
test_lru = LRUCache(3, 1, thread_safe=True)
```

## Further Example

### Backported with Django

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

### Backported with Flask

For simple usage in Flask probably occured by using the LRUCache decorators on top of the router flask decorator. Ensure you've already installed Flask with `pip install flask` and then create new file such as the following example :

```python
# app.py

from flask import Flask
from lru.decorators import lru_cache_time

app = Flask(__name__)

@lru_cache_time(seconds=60)
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

After that, you can run the Flask app with the command like `python app.py` and then open it in the browser according to the existing localhost. **As for noted**, the use of the `@lru_cache_time` decorators itself will set the cache capacity and duration of the cache. Since here we only return plain text / html with *Hello World* output, i'm assume we don't need to set the cache capacity. 

Basically, in this example there's a several confusion and caveats :

- After the cache duration that we have set exceeds the maximum limit of expired time, will the value of the function be deleted or not? cause the output is not JSON type (probably i'll given a try to using the `jsonify` method or `make_response`).
- Secondly, whether the value it still be stored and appears in a web browser or not, if we stop the flask server.
- Using LRUCache decorators in Django cause a problem in the clickjacking middleware section, we can temporarily set `X-FRAME-OPTIONS` to `DENY` in `settings.py` file inside Django root project if we want to use LRUCache decorators.

Likewise, the use of LRUcache in Django or Flask itself is very limited at this time, because there is a contradiction that is we can't set the objects dynamically, and another obstacle is that if the object that we set is not in the dict type, we need to do the object hashing. Normally, using LRUCache at the web-environment level can be done with the following assumptions like :

- You want to build web-based streaming services
- You do object modeling in the database, such as creating objects for a song that is least or most recently heard.
- You set the song object with LRUCache, so that every time you open your site, that song will appear.

Another example of using this LRU cache is that you want to display a book that is most often searched by keywords, dynamically remove an object that is not or least used, store data of users who frequently visit our site and many others.

## Running the tests

For running the test, you can use command `python -m unittest tests`

## Why using this, instead of X?

Why use object cache level instead of filtering method or get method based on API? Ideally, cache is fast. and just fast as storage, reading or accessing the data from a cache takes less time than reading the data from something else. in example if you use filtering methods, you are doing accessing and getting the object from your database. Otherwise, caching the object improves performance by keeping recent or most used data in memory locations rather we're going to use computationally object from database.

## Roadmap

- [x] Use classes as decorators for caching the objects
- [x] Add expired time for caching objects
- [ ] Add thread safe parameter
- [ ] Scale the LRUCache capacity
- [ ] Backported and integrated with Django request and response
- [x] Write unittest for LRUCache


## Contributions

Since this package is still being under developed, any contributions are much welcomed and you can read on contribution page.

## License

This package is licensed under the MIT License.
