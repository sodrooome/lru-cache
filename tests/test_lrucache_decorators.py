"""Unit tests for LRUCache decorators"""

import unittest
from unittest.mock import patch
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
        self.assertEqual(foo(5), 10)

    def test_lru_cache_returns_correct_value(self):
        @lru_cache(capacity=3)
        def foo(x):
            return x * 2

        self.assertEqual(foo(5), 10)
        self.assertEqual(foo(0), 0)
        self.assertEqual(foo(-3), -6)

    def test_lru_cache_stores_result(self):
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

    def test_lru_cache_capacity_eviction(self):
        call_count = {"value": 0}

        @lru_cache(capacity=2)
        def foo(x):
            call_count["value"] += 1
            return x * 10

        foo(1)
        foo(2)
        foo(3)

        self.assertEqual(call_count["value"], 3)
        foo(1)
        self.assertEqual(call_count["value"], 4)

    def test_lru_cache_distinguishes_args(self):
        call_count = {"value": 0}

        @lru_cache(capacity=5)
        def foo(x, y):
            call_count["value"] += 1
            return x + y

        self.assertEqual(foo(1, 2), 3)
        self.assertEqual(foo(2, 1), 3)
        self.assertEqual(call_count["value"], 2)

        self.assertEqual(foo(1, 2), 3)
        self.assertEqual(foo(2, 1), 3)
        self.assertEqual(call_count["value"], 2)

    def test_lru_cache_expiry_time(self):
        initial_call = 0

        fake_datetime = datetime(2026, 9, 5, 0, 0)

        with patch("lru.decorators.datetime") as mock_datetime:
            mock_datetime.utcnow.return_value = fake_datetime

            @lru_cache_time(capacity=3, seconds=30)
            def foo(x):
                nonlocal initial_call
                initial_call += 1
                return x * 2

            self.assertEqual(foo(2), 4)
            self.assertEqual(initial_call, 1)

            mock_datetime.utcnow.return_value = fake_datetime + timedelta(seconds=10)

            self.assertEqual(foo(2), 4)
            self.assertEqual(initial_call, 1)

            mock_datetime.utcnow.return_value = fake_datetime + timedelta(seconds=31)

            self.assertEqual(foo(2), 4)
            self.assertEqual(initial_call, 2)

    def test_lru_cache_time_caches_within_ttl(self):
        call_count = {"value": 0}
        fake_datetime = datetime(2026, 9, 5, 0, 0)

        with patch("lru.decorators.datetime") as mock_datetime:
            mock_datetime.utcnow.return_value = fake_datetime

            @lru_cache_time(capacity=3, seconds=60)
            def foo(x):
                call_count["value"] += 1
                return x + 1

            self.assertEqual(foo(10), 11)
            self.assertEqual(call_count["value"], 1)

            mock_datetime.utcnow.return_value = fake_datetime + timedelta(seconds=30)
            self.assertEqual(foo(10), 11)
            self.assertEqual(call_count["value"], 1)

    def test_lru_cache_time_different_args_separate_entries(self):
        call_count = {"value": 0}
        fake_datetime = datetime(2026, 9, 5, 0, 0)

        with patch("lru.decorators.datetime") as mock_datetime:
            mock_datetime.utcnow.return_value = fake_datetime

            @lru_cache_time(capacity=5, seconds=60)
            def foo(x):
                call_count["value"] += 1
                return x * 2

            self.assertEqual(foo(1), 2)
            self.assertEqual(foo(2), 4)
            self.assertEqual(call_count["value"], 2)

            self.assertEqual(foo(1), 2)
            self.assertEqual(foo(2), 4)
            self.assertEqual(call_count["value"], 2)


if __name__ == "__main__":
    unittest.main()
