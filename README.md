# LRU Cache

 ![PyPI - Status](https://img.shields.io/pypi/status/lruheap) [![Downloads](https://pepy.tech/badge/lruheap)](https://pepy.tech/project/lruheap) [![codecov](https://codecov.io/gh/sodrooome/lru-cache/branch/master/graph/badge.svg)](https://codecov.io/gh/sodrooome/lru-cache)

**LRUCache** is a Python package for in-memory caching using the LRU (Least Recently Used) eviction policy. Unlike Python’s built-in `OrderedDict`-based approach, this implementation uses a min-heap priority queue to track access times, providing efficient eviction of the least recently used entry when the cache reaches capacity.

**Features**

- Zero dependencies with pure Python, no external libraries
- Granular TTL (time-to-live) expiration per cache entry
- Optional thread-safe mode via `threading.RLock`
- Cache introspection methods: inspect capacity, TTL, and contents at runtime
- Decorator-based caching for function return values

## Usage

LRUCache only works in Python version 3.10 and above, you can install it with :

```sh
pip install lruheap
```

or, with `uv` package manager to faster installation :

```sh
uv pip install lruheap
```

## Documentation

You can read the fully detailed explanation about this package in [here](https://lru-cache.readthedocs.io/en/latest/)

## Contribution

Any contributions are much welcomed, and you can read on contribution page on how to contribute.

## License

This package is licensed under the MIT License.
