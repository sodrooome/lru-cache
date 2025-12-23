======
Guides
======

.. image:: https://pepy.tech/badge/lruheap
    :target: https://pepy.tech/badge/lruheap
    :alt: Download

.. image:: https://img.shields.io/pypi/status/lruheap
    :target: https://img.shields.io/pypi/status/lruheap
    :alt: Status package

.. image:: https://codecov.io/gh/sodrooome/lru-cache/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/sodrooome/lru-cache/branch/master/graph/badge.svg
    :alt: Code coverage

**LRUCache** is a package for tracking store in-data memory using replacement cache algorithm / LRU cache. The Priority of storing or removing the data based on Min-Max heap algorithm or basic priority queue instead using **OrderedDict** module that provided by Python.

Installation
------------

.. warning::
    Compatibility version
    --------------------- 
    Since the version of 1.1.0, this package only support Python 3.10 and above, so please make sure your Python version is compatible with this package

**LRUCache** has been published on PyPI and already stable since version 1.0.1, you can install it using following command :

.. code-block:: bash
    
    pip install lruheap


Usage
-----

A simple usage of **LRUCache** package can be executed as follows 

.. code-block:: python

    from lru.lrucache import LRUCache

    lru_cache = LRUCache(capacity=5)
    lru_cache.set(1, "test1")
    lru_cache.get(1) # will return "test1"

And that's it! you can explore more about this package in the **Usage** guide

Testing
-------

For running the test, you can use command `python -m unittest tests` or `python -m unittest discover .`