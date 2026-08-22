"""Unit tests for the version module in lru/version.py"""

import unittest
from lru import version
from lru.version import get_version, get_version_as_tuple


class TestVersion(unittest.TestCase):
    """Test cases covering the version module public API"""

    def test_get_version_returns_string(self):
        result = get_version()
        self.assertIsInstance(result, str)
        self.assertRegex(result, r"^\d+\.\d+\.\d+$")

    def test_get_version_matches_module_constant(self):
        self.assertEqual(get_version(), version.__version__)

    def test_get_version_as_tuple_returns_ints(self):
        result = get_version_as_tuple()
        self.assertIsInstance(result, tuple)
        for component in result:
            self.assertIsInstance(component, int)

    def test_get_version_as_tuple_matches_string(self):
        str_version = get_version()
        tuple_version = get_version_as_tuple()
        self.assertEqual(".".join(map(str, tuple_version)), str_version)

    def test_get_version_as_tuple_has_three_components(self):
        result = get_version_as_tuple()
        self.assertEqual(len(result), 3)


if __name__ == "__main__":
    unittest.main()
