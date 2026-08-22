"""Module for unittest."""

import threading
import unittest
import time
import warnings
from unittest.mock import MagicMock
from lru.lrucache import LRUCache
from lru.heap import Heap


class LRUCacheTest(unittest.TestCase):
    """Initial class for unittest. The test is
    pretty simple, only using True and False expression.
    """

    def setUp(self):
        self.testLRU = LRUCache(3)
        self.testLRU.set(1, "test1")
        self.testLRU.set(2, "test2")
        self.testLRU.set(3, "test3")

    def tearDown(self):
        self.testLRU = None

    def test_get_cache_key(self):
        self.assertIn(1, self.testLRU)
        self.assertNotIn(4, self.testLRU)

    def test_get_cache_dict(self):
        self.assertTrue(self.testLRU.get_dict())

    def test_check_whether_cache_is_empty(self):
        self.testLRU.clear_all()
        self.assertTrue(self.testLRU.is_empty())

    def test_get_cache_duration(self):
        self.assertTrue(self.testLRU.get_duration(expired_time=3600))
        self.assertFalse(self.testLRU.get_duration(expired_time=100))

    def test_get_least_recently_used(self):
        self.assertTrue(self.testLRU.get_lru_element())

    def test_get_ttl(self):
        self.assertTrue(self.testLRU.get_ttl(1))
        self.assertFalse(self.testLRU.get_ttl(key=5))

    def test_cache_is_empty(self):
        self.assertFalse(self.testLRU.is_empty())

    def test_remove_the_cache(self):
        self.assertIsNone(self.testLRU.clear_all())

    def test_remove_the_cache_key(self):
        self.assertIsNone(self.testLRU.clear_cache_key(1))

    def test_get_capacity(self):
        self.assertTrue(self.testLRU.get_capacity())

    def test_get_time_to_live(self):
        self.assertEqual(self.testLRU.ttl, 900)

    def test_string_output_for_cache(self):
        self.assertTrue(self.testLRU.__str__())

    def test_set_new_object(self):
        self.testLRU.set(1, "updated test")
        self.assertEqual(self.testLRU.get(1), "updated test")

    def test_scale_capacity(self):
        self.assertTrue(self.testLRU(capacity=300))

    def test_cache_length_method(self):
        self.assertEqual(self.testLRU.__len__(), 3)

    def test_get_key_update_access_time(self):
        # mocking time for testing purposes, this test
        # only test whether the access time is updated
        # when getting the cache key, and only verified
        # returned values from MagicMock and mutated values
        cache = LRUCache()
        cache.lock = MagicMock()

        fresh_time = time.perf_counter()
        cache._cache_dict = {1: ("key", fresh_time)}

        cache._has_key = MagicMock(return_value=True)
        cache.cache = MagicMock()

        value = cache.get(1)
        self.assertEqual(value, "key")

        _, updated_time = cache._cache_dict[1]
        self.assertGreaterEqual(updated_time, fresh_time)

    def test_get_raises_on_expired_key(self):
        # get() must raise KeyError and evict
        # the entry when TTL has elapsed
        cache = LRUCache(capacity=10, seconds=1)
        cache.set(42, "haha")

        value, _ = cache._cache_dict[42]
        # simulate the TTL elapsing based on the
        # sorted timestamp. 2 seconds > 1 second
        cache._cache_dict[42] = (value, time.perf_counter() - 2)

        with self.assertRaises(KeyError):
            cache.get(42)

        self.assertNotIn(42, cache)

    def test_set_evicts_lru_when_capacity_full(self):
        cache = LRUCache(capacity=3, seconds=900)
        cache.set(1, "a")
        cache.set(2, "b")
        cache.set(3, "c")

        # access key 1 so it becomes most recently used,
        # making key 2 the LRU candidate for eviction
        cache.get(1)

        cache.set(4, "d")

        self.assertNotIn(2, cache)
        self.assertIn(1, cache)
        self.assertIn(3, cache)
        self.assertIn(4, cache)

    def test_set_updates_existing_key_in_place(self):
        cache = LRUCache(capacity=3)
        cache.set(1, "a")
        cache.set(1, "b")

        self.assertEqual(len(cache), 1)
        self.assertEqual(cache.get(1), "b")

    def test_get_ttl_evicts_expired_entry(self):
        cache = LRUCache(capacity=10, seconds=1)
        cache.set(7, "value")

        value, _ = cache._cache_dict[7]
        # simulate TTL elapsing: 2 seconds ago > 1 second TTL
        cache._cache_dict[7] = (value, time.perf_counter() - 2)

        self.assertFalse(cache.get_ttl(7))
        self.assertNotIn(7, cache)

    def test_get_lru_element_returns_none_when_empty(self):
        cache = LRUCache(capacity=3)
        self.assertIsNone(cache.get_lru_element())

    def test_clear_cache_key_missing_is_noop(self):
        cache = LRUCache(capacity=3)
        cache.set(1, "a")
        cache.clear_cache_key(99)
        self.assertIn(1, cache)
        self.assertEqual(len(cache), 1)

    def test_get_dict_returns_shallow_copy(self):
        cache = LRUCache(capacity=3)
        cache.set(1, "a")
        snapshot = cache.get_dict()
        snapshot[1] = "mutated"

        self.assertEqual(cache.get(1), "a")

    def test_call_returns_heap_object(self):
        cache = LRUCache(capacity=3)
        self.assertIsInstance(cache(), Heap)

    def test_get_cache_emits_deprecation_warning(self):
        cache = LRUCache(capacity=3)
        cache.set(1, "a")

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            self.assertTrue(cache.get_cache(1))
            self.assertFalse(cache.get_cache(99))

        self.assertEqual(len(caught), 2)
        self.assertTrue(issubclass(caught[0].category, UserWarning))

    def test_thread_safe_mode_uses_real_lock(self):
        cache = LRUCache(capacity=3, thread_safe=True)
        self.assertIsInstance(cache.lock, type(threading.RLock()))

    def test_thread_safe_concurrent_set_get(self):
        cache = LRUCache(capacity=128, thread_safe=True)
        threads = []

        def worker(n):
            cache.set(n, n * 2)
            self.assertEqual(cache.get(n), n * 2)

        for n in range(50):
            threads.append(threading.Thread(target=worker, args=(n,)))

        for t in threads:
            t.start()
        for t in threads:
            t.join()

        self.assertEqual(len(cache), 50)

    def test_eq_with_non_lrucache_returns_notimplemented(self):
        cache = LRUCache(capacity=3)
        # comparing against a plain object hits the NotImplemented branch;
        # Python falls back to identity comparison which is False here
        self.assertNotEqual(cache, object())


class LRUCacheTestInitialization(unittest.TestCase):
    """Initial class for unittest the initialization of LRUCache
    including the validation of the property
    """

    def test_valid_initialization(self):
        self.testLRU = LRUCache(capacity=5, seconds=60)
        self.assertEqual(self.testLRU.capacity, 5)
        self.assertEqual(self.testLRU.seconds, 60)

    def test_invalid_validation(self):
        with self.assertRaises(ValueError):
            LRUCache(capacity=-1)

        with self.assertRaises(ValueError):
            LRUCache(capacity=None)

        with self.assertRaises(ValueError):
            LRUCache(capacity=129)

        with self.assertRaises(ValueError):
            LRUCache(seconds=-10)

        with self.assertRaises(ValueError):
            LRUCache(seconds=None)

        with self.assertRaises(ValueError):
            LRUCache(seconds=60 * 15 * 15 * 15)

        with self.assertRaises(KeyError):
            cache = LRUCache(capacity=1)
            cache.get(key=1)

    def test_equality_for_cache_dict(self):
        cache_1 = LRUCache(capacity=3)
        cache_2 = LRUCache(capacity=3)
        self.assertEqual(cache_1, cache_2)

    @unittest.expectedFailure
    def test_different_equality_for_cache_dict(self):
        cache_1 = LRUCache(capacity=3)
        cache_2 = LRUCache(capacity=5)
        self.assertNotEqual(cache_1, cache_2)

    def test_hashable_cache(self):
        cache_1 = LRUCache(capacity=3)
        cache_2 = LRUCache(capacity=3)
        self.assertEqual(hash(cache_1), hash(cache_2))

    @unittest.expectedFailure
    def test_different_hashable_cache(self):
        cache_1 = LRUCache(capacity=3)
        cache_2 = LRUCache(capacity=5)
        self.assertNotEqual(hash(cache_1), hash(cache_2))
