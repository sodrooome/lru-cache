=======
Roadmap
=======

The current stable version is **1.1.0**. Here is the progress on planned
features:

Completed
---------

- [x] Use classes as decorators for caching objects
- [x] Add expired time for caching objects (TTL)
- [x] Add thread-safe parameter
- [x] Improved static type hints for all methods
- [x] Dropped support for Python below 3.10
- [x] Bug fixes in core modules (``lru.lrucache``, ``lru.heap``)

Planned / In progress
---------------------

- [ ] Scale the LRUCache capacity beyond 128
- [ ] Backport and integrate with Django request/response cycle
- [ ] Improve code coverage to 90 % for critical modules
- [ ] Fix critical bugs in the ``lru.decorators`` module

Contributions
=============

Contributors are welcome! I gladly accept any contributions to this
project. Feel free to raise an issue or submit a pull request for
improvements or bug fixes.
