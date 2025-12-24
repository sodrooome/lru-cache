============
Miscellanous
============

Why use object cache level instead of filtering method or get method based on API? Ideally, cache is fast. and just fast as storage, reading or accessing the data from a cache takes less time than reading the data from something else. in example if you use filtering methods, you are doing accessing and getting the object from your database. Otherwise, caching the object improves performance by keeping recent or most used data in memory locations rather we're going to use computationally object from database.

Purpose
-------

The purpose of using this package itself is at least to be able to dynamically tracking. inserting, and removing least frequently used in-data memory or in an element. Another purposes, with the use of python decorator or the method looks like, it's also possible to figure it out whether the data in the cache is full or not (it's called **LRU eviction**), since Min-Max heap algorithm is using **O(1)** complexity for basic insertion and searching, it's also possible to efficiently accessing the store in-data memory based on most frequently used method.