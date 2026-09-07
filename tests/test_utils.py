"""Unit tests for utility helpers in lru/utils.py"""

import unittest
from lru.utils import BypassThreadSafe, generate_hash_key


class TestBypassThreadSafe(unittest.TestCase):
    """Test cases for the BypassThreadSafe no-op context manager"""

    def test_enter_returns_none(self):
        ctx = BypassThreadSafe()
        with ctx as obj:
            self.assertIsNone(obj)

    def test_exit_returns_none(self):
        ctx = BypassThreadSafe()
        # __exit__ should not suppress exceptions
        result = ctx.__exit__(None, None, None)
        self.assertIsNone(result)

    def test_exit_does_not_suppress_exceptions(self):
        ctx = BypassThreadSafe()
        with self.assertRaises(ValueError):
            with ctx:
                raise ValueError("should propagate")

    def test_can_be_reused_across_multiple_with_blocks(self):
        ctx = BypassThreadSafe()
        with ctx:
            pass
        with ctx:
            pass
        # no exception means success


class TestGenerateHashKey(unittest.TestCase):
    """Test cases for the generate_hash_key helper function"""

    def test_no_arguments(self):
        key = generate_hash_key()
        self.assertIsInstance(key, int)

    def test_positional_arguments(self):
        key = generate_hash_key(1, "hello", 3.14)
        self.assertIsInstance(key, int)

    def test_keyword_arguments(self):
        key = generate_hash_key(a=1, b=2)
        self.assertIsInstance(key, int)

    def test_same_args_produce_same_hash(self):
        k1 = generate_hash_key(1, 2, x=3)
        k2 = generate_hash_key(1, 2, x=3)
        self.assertEqual(k1, k2)

    def test_different_args_produce_different_hash(self):
        k1 = generate_hash_key(1, 2)
        k2 = generate_hash_key(3, 4)
        self.assertNotEqual(k1, k2)

    def test_kwarg_order_does_not_affect_hash(self):
        # kwargs are sorted internally, so order should not matter
        k1 = generate_hash_key(a=1, b=2)
        k2 = generate_hash_key(b=2, a=1)
        self.assertEqual(k1, k2)

    def test_mixed_args_and_kwargs(self):
        key = generate_hash_key(1, 2, name="test", flag=True)
        self.assertIsInstance(key, int)


if __name__ == "__main__":
    unittest.main()
