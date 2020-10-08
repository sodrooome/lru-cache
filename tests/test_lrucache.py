"""Module for unittest."""

import unittest
# from nose.tools import raises # noqa
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
    