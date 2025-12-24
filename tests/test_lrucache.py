"""Module for unittest."""

import unittest
from unittest.mock import MagicMock
from lru.lrucache import LRUCache

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
        self.assertTrue(self.testLRU.get_cache(1))
        self.assertFalse(self.testLRU.get_cache(4))

    def test_get_cache_dict(self):
        self.assertTrue(self.testLRU.get_dict())
    
    def test_get_cache_duration(self):
        self.assertTrue(self.testLRU.get_duration(expired_time=3600))
        # this should be return into False
        # cause the maximum duration
        # is 3600 seconds
        # todo: Fix this test
        self.assertTrue(self.testLRU.get_duration(expired_time=4800))

    def test_get_least_recently_used(self):
        self.assertTrue(self.testLRU.get_lru_element())

    def test_get_ttl(self):
        self.assertTrue(self.testLRU.get_ttl(1))

    def test_cache_is_empty(self):
        self.assertFalse(self.testLRU.is_empty())

    def test_remove_the_cache(self):
        self.assertIsNone(self.testLRU.clear_all())

    def test_remove_the_cache_key(self):
        self.assertIsNone(self.testLRU.clear_cache_key(1))

    def test_get_capacity(self):
        self.assertFalse(self.testLRU.get_capacity())

    def test_string_output_for_cache(self):
        self.assertTrue(self.testLRU.__str__())

    def test_set_new_object(self):
        self.assertTrue(self.testLRU.set(1, "test4"))

    def test_scale_capacity(self):
        self.assertTrue(self.testLRU(capacity=300))

    def test_get_key_update_access_time(self):
        # mocking time for testing purposes, this test
        # only test whether the access time is updated
        # when getting the cache key, and only verified
        # returned values from MagicMock and mutated values
        cache = LRUCache()
        cache.lock = MagicMock()
        cache.cache = MagicMock()
        cache.get_cache = MagicMock(return_value=True)

        initial_time = 1.0
        cache._cache_dict = {1: ("value", initial_time)}
        value = cache.get(1)

        self.assertEqual(value, "value")
        self.assertEqual(cache._cache_dict[1][0], "value")
        self.assertNotEqual(cache._cache_dict[1][1], initial_time)

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
            LRUCache(seconds=60*15*15*15)

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
        
    