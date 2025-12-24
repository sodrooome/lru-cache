=====
Usage
=====

There is a little explanation regarding the use of this LRUcache package. You can see at this simple configuration and explanation for using several method that provided by this package.

LRUCache class initialization
-----------------------------

For the first time, you can initialize LRUCache method with maximum capacity of cache is **128** and maximum duration of cache is **15** minutes when you don't initialize at first. For example:

.. code-block:: python

    from lru.lrucache import LRUCache
    foo = LRUCache(3)

    # or you can pass the capacity and duration of cache
    foo = LRUCache(capacity=3, seconds=5*15)


`set` method
------------

Set an objects that wants to be cached in cache element, given the `key` parameters and `value` parameters as integer. For example:

.. code-block:: python

    foo.set(1, "foobar")
    foo.set(2, "bar")


`get` method
------------

Get the objects based on their key in cache element and access time, given the `key` parameters as integer. This **get()** method can also be used to tracking which objects are often called which will later be identified as recently used objects in a cache element, an object that is often called by this method will be placed in front of the cache element by using `get_lru_element()`. For example:

.. code-block:: python

    foo.get(1)
    foo.get(1) # you can iterate for calling an object
    foo.get(2)


`get_dict` method
-----------------

Method for returned a all dictionary of an object in cache element. For example:

.. code-block:: python

    foo.get_dict()


`get_duration` method
---------------------

Method for getting duration of cache, return **True** if the duration is exceed for expired time otherwise return **False** when the duration is even or below the expired time. The expired time set as 3600 seconds. For example:

.. code-block:: python

    # will return True if the duration
    # of cache is still under the
    # expired time
    foo.get_duration()


`get_lru_element` method
------------------------

Method for retrieved an object based on their key in cache element and the duration when accessing onto the dictionary. 
If the object is not called by the **get()** method, then objects that have short time for accessing onto dictionary will be placed in beginning of the cache element, if the object is called by the **get()** method, it will placed depending how many objects are called. In this case, this called as recently used. For example:

.. code-block:: python

    foo.get_lru_element()


`get_capacity` method
---------------------

Get cache capacity, return **True** if the cache is full otherwiser return **False** when the cache is not full. For example:

.. code-block:: python

    foo.get_capacity()


`get_cache` method
------------------

Get cache in element based on their key, return **True** if the element has a key, otherwise return **False** when element hasn't a key. Given the `key` parameters as integer. For example:

.. code-block:: python

    foo.get_cache(1)


`get_ttl` method
----------------

Get time-to-live (TTL) duration for cache, will return a value, where the value is the remaining time from the cache duration that has been set previously. Given the `key` parameters as integer. Th countdown time will be reduced by one second according to the cache duration that we have set before, if you set it to within 5 seconds, when using this method it will display a value of 4 which means its the remaining duration of our cache, and so on until the result displayed is set as`None`. For example:

.. code-block:: python

    foo.get_ttl(1)


`clear_all` method
------------------

Remove all cache in element. For example:

.. code-block:: python

    foo.clear_all()


`clear_cache_key` method
------------------------

Remove cache in element based on their key. Given the `key` as parameters for remove the cache objects. For example:

.. code-block:: python

    # this will remove cache
    # object based on first index
    foo.clear_cache_key(1)


`is_empty` method
-----------------

Check whether the current cache in element is empty or not. Will return **True** if the cache element is empty and **False** when the cache element is full of objects. For example:

.. code-block:: python

    foo.is_empty()


`@lru_cache` decorator
----------------------

Python decorators using LRUCache classes for cache an object within a function. Default capacity is 128 if you not define it. For example:

.. code-block:: python

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

`@lru_cache_time` decorator
---------------------------

.. danger::
    This is still in experimental features and under developed, there might be some bugs or unexpected results,
    if you want to try it and there is an error or an unexpected result, please raise the issue.

Python decorators for LRUCache classes using expired cached time, for example :

.. code-block:: python

    from lru.decorators import lru_cache_time

    @lru_cache_time(capacity=5, seconds=15)
    def test_lru(x):
        print("Calling f(" + str(x) + ")")
        return x

    test_lru.set(1, "foo")
    test_lru.set(2, "test")


The difference between set duration of cache if using decorators or not lies when we set the value of the duration cache. By using these **@lru_cache_time** decorators at least it will compact and dynamically clear the cache if the duration exceeds of the maximum duration (15 minutes).

Enable `thread_safe` parameter
------------------------------

By enabling **thread_safe** parameter into `True`, it will be possible to safely to call a function together. For example, if we create a shared task (functions a and b) where the shared task invokes a resource such as object from function c, then the object can safely be called and can be execute on both functions a and b (thus, its called a deadlock if we dont use **thread_safe** parameter to execute two functions from one resource). **As for concerns**, the use of **thread_safe** might be reduce the performance. For example:

.. code-block:: python

    test_lru = LRUCache(3, 1, thread_safe=True)

.. hint::
    **thread_safe** parameter
    -------------------------
    Since the version of 1.1.0, when the **thread_safe** parameter is enabled, all the methods that provided by LRUCache class will be thread-safe.
    This is a breaking change compared to the previous version
