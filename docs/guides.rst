======
Guides
======

.. image:: https://pepy.tech/badge/lruheap
    :target: https://pepy.tech/badge/lruheap
    :alt: Downloads

.. image:: https://img.shields.io/pypi/pyversions/lruheap
    :target: https://img.shields.io/pypi/pyversions/lruheap
    :alt: PyPI - Python Version

.. image:: https://img.shields.io/pypi/status/lruheap
    :target: https://img.shields.io/pypi/status/lruheap
    :alt: Status

.. image:: https://img.shields.io/pypi/types/lruheap
    :target: https://img.shields.io/pypi/types/lruheap
    :alt: PyPI - Types

.. image:: https://codecov.io/gh/sodrooome/lru-cache/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/sodrooome/lru-cache/branch/master/graph/badge.svg
    :alt: Code coverage

**LRUCache** is a Python package for in-memory caching using the LRU (Least
Recently Used) eviction policy. Unlike Python's built-in ``OrderedDict``-based
approach, this implementation uses a **min-heap priority queue** to track
access times, providing efficient eviction of the least recently used entry
when the cache reaches capacity.

Features
--------

- Zero dependencies with pure Python, no external libraries
- Granular TTL (time-to-live) expiration per cache entry
- Optional thread-safe mode via ``threading.RLock``
- Cache introspection: inspect capacity, TTL, and contents at runtime
- Decorator-based caching for function return values

Installation
------------

.. warning::
    Since version 1.1.0, this package requires Python 3.10 or above.
    Please ensure your Python version is compatible.

**LRUCache** is published on PyPI as ``lruheap``. Install it with:

.. code-block:: bash

    pip install lruheap

Or with ``uv`` for faster installation:

.. code-block:: bash

    uv pip install lruheap

Import
------

The package name on PyPI is ``lruheap``, but the Python module is ``lru``:

.. code-block:: python

    from lru.lrucache import LRUCache
    from lru.decorators import lru_cache, lru_cache_time

Quickstart
----------

.. code-block:: python

    from lru.lrucache import LRUCache

    cache = LRUCache(capacity=5)
    cache.set(1, "test1")
    print(cache.get(1))  # "test1"

See the **Usage** page for a complete API reference.

Testing
-------

Run tests with:

.. code-block:: bash

    python -m pytest tests

Or using the project Makefile:

.. code-block:: bash

    make coverage
