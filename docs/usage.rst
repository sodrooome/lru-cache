=====
Usage
=====

This page covers the complete API of the ``LRUCache`` class and the
``@lru_cache`` / ``@lru_cache_time`` decorators.

LRUCache class initialization
-----------------------------

The default capacity is **128** entries and the default TTL is **15 minutes**
(900 seconds). Both can be configured at construction time:

.. code-block:: python

    from lru.lrucache import LRUCache

    # Default: capacity=128, seconds=900
    cache = LRUCache()

    # Custom capacity and TTL
    cache = LRUCache(capacity=3, seconds=300)

.. note::

    - ``capacity`` must be an integer between ``0`` and ``128`` (inclusive).
    - ``seconds`` must be an integer between ``0`` and ``900`` (15 minutes).

``set`` method
--------------

Insert or update a cache entry. If the key already exists, its access time
is refreshed. If the cache is at capacity, the least recently used entry is
evicted first.

.. code-block:: python

    cache.set(1, "foobar")
    cache.set(2, "bar")

:param key: integer key for the entry
:param value: value to store (any type)
:returns: the internal cache dictionary

``get`` method
--------------

Retrieve the value for a given key. Calling ``get`` also updates the entry's
access time, marking it as recently used.

.. code-block:: python

    value = cache.get(1)  # "foobar"

:param key: integer key to look up
:raises KeyError: if the key is not present in the cache
:returns: the stored value

``get_dict`` method
-------------------

Return the internal cache dictionary, where keys are the integer cache keys
and values are ``(stored_value, access_time)`` tuples.

.. code-block:: python

    cache.get_dict()

:returns: dict — the full cache contents

``get_duration`` method
-----------------------

Check whether the configured cache duration (``self.seconds``) is within
the given ``expired_time`` limit. Returns ``True`` if the cache's TTL setting
is less than or equal to ``expired_time``, otherwise ``False``.

.. code-block:: python

    # Returns True if cache.seconds <= 3600
    cache.get_duration(expired_time=3600)

:param expired_time: threshold in seconds (default 3600)
:returns: bool

``get_lru_element`` method
--------------------------

Return the least recently used entry from the cache (the element at the
top of the min-heap). This is the entry that will be evicted next when
the cache reaches capacity.

.. code-block:: python

    cache.get_lru_element()

:returns: ``(value, access_time)`` tuple of the LRU entry

``get_capacity`` method
-----------------------

Check whether the cache is full. Returns ``True`` if ``len(cache) >= capacity``,
otherwise ``False``.

.. code-block:: python

    cache.get_capacity()

:returns: bool

``get_cache`` method
--------------------

Check whether a specific key exists in the cache.

.. code-block:: python

    cache.get_cache(1)

:param key: integer key
:returns: ``True`` if the key exists, ``False`` otherwise

``get_ttl`` method
------------------

Get the remaining time-to-live (in seconds) for a specific cache entry. If
the key does not exist or the TTL has expired, returns ``False``.

.. code-block:: python

    cache.get_ttl(1)

:param key: integer key
:returns: ``int`` (remaining seconds) or ``False`` if missing/expired

``clear_all`` method
--------------------

Remove all entries from the cache.

.. code-block:: python

    cache.clear_all()

``clear_cache_key`` method
--------------------------

Remove a specific entry by key.

.. code-block:: python

    cache.clear_cache_key(1)

:param key: integer key to remove

``is_empty`` method
-------------------

Check whether the cache contains any entries. Returns ``True`` if empty,
``False`` otherwise.

.. code-block:: python

    cache.is_empty()

:returns: bool

``ttl`` property
----------------

Read-only property that returns the configured TTL duration (in seconds).

.. code-block:: python

    cache.ttl  # 900 (default)

Special methods
---------------

.. code-block:: python

    len(cache)      # number of entries
    str(cache)      # string representation of the cache dict
    cache == other  # equality comparison (compares cache dicts)
    hash(cache)     # hash based on cache contents
    cache()         # returns the underlying Heap instance

``@lru_cache`` decorator
-------------------------

A decorator that wraps a function with an ``LRUCache`` instance. Function
arguments are hashed into a stable integer key; subsequent calls with the
same arguments return the cached result instead of re-executing the function.

.. code-block:: python

    from lru.decorators import lru_cache

    @lru_cache(capacity=5)
    def expensive_function(x):
        print(f"Computing f({x})...")
        return x * 2

    # First call computes and caches
    print(expensive_function(3))  # prints "Computing f(3)..." then 6

    # Second call returns cached result
    print(expensive_function(3))  # just prints 6 (no "Computing...")

    # Different arguments compute anew
    print(expensive_function(5))  # prints "Computing f(5)..." then 10

:param capacity: maximum number of cached return values (default 128)
:param kwargs: additional keyword arguments forwarded to ``LRUCache``

``@lru_cache_time`` decorator
-----------------------------

.. danger::
    This is experimental. There may be bugs or unexpected behaviour.
    If you encounter issues, please file a report on GitHub.

A decorator that wraps a function with an ``LRUCache`` instance and
**automatically clears the entire cache** once a global TTL window expires.
The expiration window resets after each clear.

.. code-block:: python

    from lru.decorators import lru_cache_time

    @lru_cache_time(capacity=5, seconds=60)
    def expensive_function(x):
        print(f"Computing f({x})...")
        return x * 2

    # All cached entries are invalidated after 60 seconds
    # regardless of individual entry age

:param capacity: maximum number of cached entries (default 128)
:param seconds: global cache TTL in seconds before full invalidation (default 900)
:param kwargs: additional keyword arguments forwarded to ``LRUCache``

Enable ``thread_safe`` parameter
---------------------------------

When ``thread_safe=True`` is passed to the ``LRUCache`` constructor, all
cache operations are protected by a ``threading.RLock``, making them safe
to call from multiple threads concurrently. This prevents race conditions
when the same cache is shared across threads.

.. code-block:: python

    from lru.lrucache import LRUCache

    cache = LRUCache(capacity=3, seconds=60, thread_safe=True)

.. hint::
    Since version 1.1.0, enabling ``thread_safe`` makes **all** methods on
    the ``LRUCache`` class thread-safe. This was a breaking change from
    earlier versions.

**Performance note:** Enabling thread safety introduces lock overhead,
which may reduce throughput. Only enable it when the cache is accessed
from multiple threads.
