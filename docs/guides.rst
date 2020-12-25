======
Guides
======

**LRUCache** is a package for tracking store in-data memory using replacement cache algorithm / LRU cache. The Priority of storing or removing the data based on Min-Max heap algorithm or basic priority queue instead using **OrderedDict** module that provided by Python.

Purpose
-------

The purpose of using this package itself is at least to be able to dynamically tracking. inserting, and removing least frequently used in-data memory or in an element. Another purposes, with the use of python decorator or the method looks like, it's also possible to figure it out whether the data in the cache is full or not (it's called **LRU eviction**), since Min-Max heap algorithm is using **O(1)** complexity for basic insertion and searching, it's also possible to efficiently accessing the store in-data memory based on most frequently used method.

Installation
------------

LRUCache only works in Python version 3.5 and above, you can install it with :

.. code-block:: bash
    
    pip3 install lruheap

**As for concerns**, since the latest version (v1.0.1), this package only support Python version 3.6 and above, the next release it will be dropped the Python 3.5 support

Testing
-------

For running the test, you can use command `python -m unittest tests`