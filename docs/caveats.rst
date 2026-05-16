=======
Caveats
=======

``lruheap`` is a lightweight, in-memory cache. While useful in many
scenarios, it has important limitations you should be aware of.

Known limitations
-----------------

1. **In-memory only, not persisted**. All data is stored in the process's memory. The cache is lost when the
   process exits or restarts. There is no on-disk persistence or replication.
2. **Not shared between processes**. Each Python process (for example: each Django/Flask worker, each Gunicorn
   worker) has its own independent cache instance. Cache entries set in
   one worker are not visible to another. This makes it unsuitable as a primary cache layer in multi-process web serving environments.
3. **TTL is checked on access, not proactively**. TTL (time-to-live) is validated when ``get()`` or ``get_ttl()`` is called.
   Expired entries are not removed by a background thread, they remain in
   memory until accessed or evicted.
4. **Not recommended for production web caching**. For production web environments, use a dedicated caching layer such as:

   - `Django's locmemcache`_ (for single-process dev) or a proper backend
   - `Redis`_ / `memcached`_ (for multi-worker production deployments)

5. **Django clickjacking middleware**. When using the ``LRUCache`` decorators with Django, you may encounter
   issues with the ``X-Frame-Options`` middleware. As a workaround, set
   ``X-FRAME-OPTIONS = 'DENY'`` in your Django ``settings.py``.

When is it suitable?
--------------------

Despite the limitations above, ``lruheap`` is a good fit for:

- **Internal tools** and scripts that run in a single process
- **Development environments** where you want lightweight caching without
  standing up a Redis or memcached instance
- **Function-level memoization** such as cache the result of expensive
  computations, API calls, or data transformations within the lifetime
  of a process

If you need to share cache state across workers or persist data across
restarts, consider using Redis, memcached, or a database-backed cache
instead.

.. _Django's locmemcache: https://docs.djangoproject.com/en/stable/topics/cache/#local-memory-caching
.. _Redis: https://redis.io
.. _memcached: https://memcached.org