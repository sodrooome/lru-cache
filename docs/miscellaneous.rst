=============
Miscellaneous
=============

Why object-level caching instead of database filtering?
-------------------------------------------------------

Cache is fast. Reading data from an in-memory cache takes significantly
less time than querying a database or calling an external API. Every time
you filter or query your database, you pay the cost of:

1. Network round-trip (if the database is remote)
2. Query parsing and planning
3. Disk I/O (if data is not in the database's own buffer pool)
4. Serialisation / deserialisation

Object-level caching avoids these costs by keeping recently or frequently
accessed data in the application process's memory.

Purpose of this package
-----------------------

The primary goal of ``lruheap`` is to provide a simple, zero-dependency
way to track, insert, and evict cache entries using the LRU policy.

When the cache reaches its capacity, the **least recently used** entry is
evicted automatically. This is determined by the entry's access time,
the oldest access time is evicted first. The underlying data structure is a **min-heap** (not a "min-max heap").
Heap operations have the following complexities:

- **Insert** (``push``): O(log n)
- **Remove minimum** (``pop``): O(log n)
- **Search by key**: O(n) in the worst case
- **Update access time**: O(n) to find the element, then O(log n) to
  re-heapify

This is different from Python's ``OrderedDict`` approach, which offers
O(1) move-to-end operations but doesn't natively support TTL expiration.
The min-heap approach gives us efficient access to the LRU element (the
minimum) and a natural structure for adding time-based eviction.
