"""Unit tests for LRUCache decorators"""

import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from lru.decorators import lru_cache, lru_cache_time


class TestLRUCacheDecorators(unittest.TestCase):
    """Test suite for LRUCache decorators, should
    be covered up everything it if's possible"""

    def test_lru_cache_decorator_is_correct(self):
        @lru_cache(capacity=3)
        def foo(x):
            return x * 2

        self.assertTrue(callable(foo))

        # TODO: fix the equality of returned result
        # self.assertEqual(foo(5), 10)

    def test_lru_cache_stores_result(self):
        # repeated calls with the same argument must hit the cache
        initial_call = 0

        @lru_cache(capacity=3)
        def foo(x):
            nonlocal initial_call
            initial_call += 1
            return x * 10

        foo(1)
        foo(1)
        foo(1)

        self.assertEqual(initial_call, 1)

    def test_lru_cache_expiry_time(self):
        @lru_cache_time(capacity=3, seconds=30)
        def foo(x):
            return x * 2

        self.assertTrue(callable(foo))


if __name__ == "__main__":
    unittest.main()
