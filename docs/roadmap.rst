=======
Roadmap
=======

Apparently, this project has been discontinued around 3 years, but with the current latest version of **1.1.0**, there are several breaking changes
and major improvements such as:

- Enabling **thread_safe** parameter will make all methods in LRUCache class thread-safe
- Dropping support for Python version below 3.10
- Improved static type hints for all methods in `lru.lrucache` module
- Fixed a few of bugs in `lru.lrucache` module which causing unexpected behavior and can't function properly

However, since this package already at stable version **(v1.0.1)** around 3 years ago, so for next update there will be improvements in several features such as :

.. |check| raw:: html

    <input checked=""  type="checkbox">

.. |uncheck_| raw:: html

    <input disabled="" type="checkbox">

- |check| Use classes as decorators for caching the objects
- |check| Add expired time for caching objects
- |check| Add thread safe parameter
- |uncheck_| Scale the LRUCache capacity
- |uncheck_| Backported and integrated with Django request and response
- |uncheck_| Improve code coverage up to 90 % for critical modules
- |uncheck_| Fixed critical bugs in the `lru.decorators` module

Contributions
=============

Contributors are welcome and I gladly accept any contributions to this project. Feel free to raise an issue or a pull request for any improvements or
bug fixes that you want to contribute.
