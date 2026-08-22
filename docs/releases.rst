===============
Release History
===============

v1.3.1 (2026-08-22)
-------------------

.. rubric:: Bug fixes

- Fixed ``__eq__`` guard using ``isinstance(other, object)`` which is always ``True``, making the ``NotImplemented`` branch unreachable and causing ``AttributeError`` when comparing against non-``LRUCache`` objects

.. rubric:: Improvements

- Improved test coverage from 94 % to 100 % for core modules (``lru.lrucache``, ``lru.heap``, ``lru.version``, ``lru.utils``)
- Added test cases covering ``LRUCache`` capacity eviction, TTL expiry on ``get_ttl()``, empty ``get_lru_element()``, ``clear_cache_key()`` no-op, ``get_dict()`` shallow copy, ``__call__`` and deprecation warning for ``get_cache()``
- Added tests covering thread-safe mode (``thread_safe=True``) with real ``RLock``
- Added tests covering ``Heap.build_push_down`` empty-heap branch and the ``Heap`` stress sequence
- Added tests covering decorator return-value correctness and capacity eviction for ``lru_cache``
- Added dedicated test modules for ``lru.version`` and ``lru.utils`` (``BypassThreadSafe`` and ``generate_hash_key``)
- Backfilled the missing v1.3.0 release notes entry

v1.3.0 (2026-08-09)
-------------------

.. rubric:: Bug fixes

- Fixed wrong child being swapped during heap ``_build_push_down_heapify`` which broke the min-heap invariant; the correct child is now swapped and recursion continues on the right side
- Fixed ``build_floyd_heap`` iterating over an integer instead of a list, raising ``TypeError`` immediately
- Fixed ``_build_push_up_heapify`` silently accessing the heap from the last element instead of skipping it
- Fixed ``remove()`` not swapping the root with the last element before popping and sifting down
- Fixed ``validate_heapify`` comparing the root against itself instead of skipping it
- Fixed correct heap object swap, validated heapify and Floyd's build

.. rubric:: Improvements

- Enforced TTL on every read; expired entries are now evicted as early as possible
- Deprecated ``get_cache()`` in favour of the ``__contains__`` protocol (``key in cache``) and ``get()``
- ``get_dict()`` now returns a shallow copy under the lock
- Safe ``get_lru_element()`` returning ``None`` on empty cache
- Extracted internal helpers ``_has_key``, ``_is_expired``, ``_evict`` to avoid the double-lock fragility of the old ``get_cache()`` call path
- Added PEP 561 marker (``py.typed``) for typed package distribution
- Added comprehensive tests for the ``Heap`` class
- Updated documentation and roadmap for the v1.3.0 API changes
- Added release history page and switched docs theme to Shibuya

v1.2.0 (2026-05-16)
-------------------

.. rubric:: Bug fixes

- Fixed falsy value bug where a cache entry existed but was treated as missing
- Fixed missing lock acquisition during ``clear_cache_key()``
- Added early guard when the last element is removed to prevent crash
- Fixed ``lru_cache_time`` decorator that bypassed caching logic and returned the ``Heap`` object
- Fixed decorator not wrapping the function; actual caching never ran

.. rubric:: Improvements

- Major rework of the documentation
- Updated documentation regarding ``thread_safe`` usage and heapify objects
- Patched unit tests for cache decorators by mocking cache time progression
- Added Makefile for easier project lifecycle management
- Patched unit tests for ``lrucache`` modules due to recent bugfixes
- Fixed inline docstrings causing parameters not to be rendered
- Wrote additional test items covering cache decorators

v1.1.0 (2025-12-24)
-------------------

.. rubric:: Breaking changes

- **Dropped Python 3.9 and below** — minimum required version is now **Python 3.10**
- ``thread_safe`` now makes **all** methods on the ``LRUCache`` class thread-safe
- Replaced ``setup.py`` with modern Python packaging (``pyproject.toml``)

.. rubric:: Bug fixes

- Fixed critical issues causing broken logic in core modules
- Fixed codecov integration requiring access token
- Fixed Python 3.10 TOML support
- Fixed inability to find codecov repository

.. rubric:: Improvements

- Overhauled documentation, fixed inline code, improved how-to guides
- Added comprehensive tests for ``LRUCache`` core functions
- Improved ``README`` with key insights about the package
- Removed unnecessary Python classifiers
- Replaced ``setup.py`` with ``pyproject.toml`` for modern Python packaging
- Overrode previous publishing infrastructure with test coverage

v1.0.2 (2021-02-16)
-------------------

- Added caveats section and upgrade requirements
- Added typing hints in methods
- Removed instructions in README, added badge
- Removed readthedocs configuration
- Changed built-in documentation and format

v1.0.1 (2020-12-15)
-------------------

- Added Python typing checker for all methods (type hints)
- Dropped Python 3.5 support
- Ignored ``.idea`` config files

v1.0.0 (2020-10-09)
-------------------

.. rubric:: First stable release.

- Bugfix for ``set`` / ``get`` methods
- Tests for ``get_lru_element()``
- Bugfix for failing Travis build
- Re-wrote documentation
- Changed documentation theme

v0.1.5 (2020-09-30)
-------------------

- Refactored heapify method to use min-max functions
- Wrote example for usage of ``LRUCache``
- Removed unused comments
- Removed maintain badge

v0.1.4 (2020-07-28)
-------------------

- Added hashable method for key in dict object
- Refactored iterative heapify method to correctly find minimum index

v0.1.3 (2020-07-18)
-------------------

- Enabled ``thread_safe`` parameter
- Added ``BypassThreadSafe`` utility class
- Added unit tests
- Refactored method signatures

v0.1.2 (2020-07-17)
-------------------

- Removed unused comments

v0.1.1 (2020-07-17)
-------------------

- Refactored heapify method to correctly find minimum index

v0.1.0 (2020-07-15)
-------------------

- Broke down decorators by introducing ``lru_cache_time``
- Added expired time (TTL) for caching objects
- Updated documentation and bumped version

v0.0.3 (2020-07-14)
-------------------

- Added decorators for caching objects
- Added ``remove_cache_key()`` method
- Fixed undefined variable in heapify method
- Concise documentation and bumped release

v0.0.2 (2020-07-13)
-------------------

- Changed access time variable to use ``perf_counter``
- Fixed ``list indices must be integers`` error in heapify

v0.0.1 (2020-07-11)
-------------------

.. rubric:: Initial release.

- Module for LRU cache with mock examples
- Fixed heapify push and down methods
- Initial commit
