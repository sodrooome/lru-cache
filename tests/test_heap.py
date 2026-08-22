"""Unit tests for the Heap class in lru/heap.py"""

import unittest
from lru.heap import Heap


class TestHeap(unittest.TestCase):
    """
    Comprehensive test cases which are covers all public
    methods on the Heap class includes behavioral validation
    """

    def setUp(self):
        self.heap = Heap()

    def test_empty_init(self):
        self.assertEqual(self.heap.heap, [])

    def test_init_with_cache_list(self):
        h = Heap([(1, 5.0), (2, 3.0), (3, 4.0)])
        self.assertEqual(len(h.heap), 3)
        self.assertTrue(h.validate_heapify())

    def test_add_single(self):
        self.heap.add(1, 5.0)
        self.assertEqual(self.heap.heap[0], (1, 5.0))

    def test_add_in_descending_order(self):
        self.heap.add(1, 5.0)
        self.heap.add(2, 4.0)
        self.heap.add(3, 3.0)
        self.assertEqual(self.heap.heap[0][1], 3.0)
        self.assertTrue(self.heap.validate_heapify())

    def test_add_out_of_order(self):
        self.heap.add(1, 10.0)
        self.heap.add(2, 5.0)
        self.heap.add(3, 20.0)
        self.heap.add(4, 1.0)
        self.assertEqual(self.heap.heap[0], (4, 1.0))
        self.assertTrue(self.heap.validate_heapify())

    def test_remove_returns_minimum(self):
        self.heap.add(1, 5.0)
        self.heap.add(2, 3.0)
        self.heap.add(3, 4.0)
        result = self.heap.remove()
        self.assertEqual(result, (2, 3.0))

    def test_remove_reduces_length(self):
        self.heap.add(1, 5.0)
        self.heap.add(2, 3.0)
        self.heap.remove()
        self.assertEqual(len(self.heap.heap), 1)

    def test_remove_maintains_heap(self):
        self.heap.add(1, 5.0)
        self.heap.add(2, 3.0)
        self.heap.add(3, 8.0)
        self.heap.add(4, 1.0)
        self.heap.add(5, 6.0)
        self.heap.remove()
        self.assertTrue(self.heap.validate_heapify())

    def test_remove_single_element(self):
        self.heap.add(1, 5.0)
        result = self.heap.remove()
        self.assertEqual(result, (1, 5.0))
        self.assertEqual(self.heap.heap, [])

    def test_remove_empty_heap_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.heap.remove()

    def test_remove_key_existing(self):
        self.heap.add(1, 5.0)
        self.heap.add(2, 3.0)
        self.heap.add(3, 4.0)
        self.heap.remove_key(1)
        keys = {k for k, _ in self.heap.heap}
        self.assertNotIn(1, keys)
        self.assertTrue(self.heap.validate_heapify())

    def test_remove_key_missing_returns_heap_unchanged(self):
        self.heap.add(1, 5.0)
        self.heap.add(2, 3.0)
        original = list(self.heap.heap)
        result = self.heap.remove_key(99)
        self.assertEqual(self.heap.heap, original)
        self.assertIs(result, self.heap.heap)

    def test_remove_key_last_element(self):
        self.heap.add(1, 5.0)
        self.heap.add(2, 3.0)
        self.heap.add(3, 4.0)
        last_key = self.heap.heap[-1][0]
        self.heap.remove_key(last_key)
        self.assertTrue(self.heap.validate_heapify())

    def test_remove_key_maintains_heap(self):
        for i in range(1, 7):
            self.heap.add(i, float(i * 2))
        self.heap.remove_key(3)
        self.heap.remove_key(5)
        self.assertTrue(self.heap.validate_heapify())

    def test_update_increase_value_sifts_down(self):
        self.heap.add(1, 5.0)
        self.heap.add(2, 3.0)
        self.heap.add(3, 4.0)
        # update key 2 (currently min at 3.0) to 10.0 and should sift down
        self.heap.update(2, 10.0)
        self.assertEqual(self.heap.heap[0][1], 4.0)
        self.assertTrue(self.heap.validate_heapify())

    def test_update_decrease_value_sifts_up(self):
        self.heap.add(1, 5.0)
        self.heap.add(2, 3.0)
        self.heap.add(3, 4.0)
        # update key 1 (currently 5.0) to 1.0 and should sift up to root
        self.heap.update(1, 1.0)
        self.assertEqual(self.heap.heap[0], (1, 1.0))
        self.assertTrue(self.heap.validate_heapify())

    def test_update_missing_key_returns_heap_unchanged(self):
        self.heap.add(1, 5.0)
        self.heap.add(2, 3.0)
        original = list(self.heap.heap)
        result = self.heap.update(99, 10.0)
        self.assertEqual(self.heap.heap, original)
        self.assertIs(result, self.heap.heap)

    def test_update_maintains_heap_after_multiple(self):
        for i in range(1, 8):
            self.heap.add(i, float(i))
        self.heap.update(4, 0.5)
        self.heap.update(7, 1.5)
        self.heap.update(2, 9.0)
        self.assertTrue(self.heap.validate_heapify())

    def test_build_floyd_heap(self):
        self.heap.heap = [(1, 10.0), (2, 5.0), (3, 8.0), (4, 1.0), (5, 3.0)]
        result = self.heap.build_floyd_heap
        self.assertTrue(self.heap.validate_heapify())
        self.assertIs(result, self.heap.heap)

    def test_validate_heapify_valid(self):
        self.heap.heap = [(2, 2.0), (4, 4.0), (3, 3.0)]
        self.assertTrue(self.heap.validate_heapify())

    def test_validate_heapify_invalid(self):
        # parent (index 0, 10.0) > left child (index 1, 5.0)
        # which is expected to be invalid
        self.heap.heap = [(1, 10.0), (2, 5.0), (3, 8.0)]
        self.assertFalse(self.heap.validate_heapify())

    def test_parent_child_indices(self):
        self.assertEqual(self.heap.parent(1), 0)
        self.assertEqual(self.heap.parent(2), 0)
        self.assertEqual(self.heap.parent(3), 1)
        self.assertEqual(self.heap.left_child(0), 1)
        self.assertEqual(self.heap.right_child(0), 2)
        self.assertEqual(self.heap.left_child(1), 3)
        self.assertEqual(self.heap.right_child(1), 4)

    def test_is_leaf(self):
        self.heap.heap = [(1, 1.0), (2, 2.0), (3, 3.0), (4, 4.0)]
        self.assertFalse(self.heap._is_leaf(0))
        self.assertFalse(self.heap._is_leaf(1))
        self.assertTrue(self.heap._is_leaf(2))
        self.assertTrue(self.heap._is_leaf(3))

    def test_build_push_down_empty_heap_uses_push_up(self):
        result = self.heap.build_push_down(0)
        self.assertEqual(result, [])
        self.assertEqual(self.heap.heap, [])

    def test_build_push_down_non_empty_uses_push_down(self):
        self.heap.heap = [(1, 5.0), (2, 10.0)]
        result = self.heap.build_push_down(0)
        self.assertIs(result, self.heap.heap)
        self.assertTrue(self.heap.validate_heapify())

    def test_stress_sequence(self):
        ops = [
            ("add", 1, 10.0),
            ("add", 2, 5.0),
            ("add", 3, 8.0),
            ("add", 4, 1.0),
            ("add", 5, 7.0),
            ("remove", None, None),  # should removes these lists (4, 1.0)
            ("add", 6, 3.0),
            ("update", 2, 12.0),  # 2 was minimum, now 12.0 and it must be sift down
            ("remove_key", 3, None),
            ("add", 7, 0.5),
        ]
        for op in ops:
            if op[0] == "add":
                self.heap.add(op[1], op[2])
            elif op[0] == "remove":
                self.heap.remove()
            elif op[0] == "update":
                self.heap.update(op[1], op[2])
            elif op[0] == "remove_key":
                self.heap.remove_key(op[1])
            self.assertTrue(
                self.heap.validate_heapify(),
                f"Heap property violated after {op}",
            )


if __name__ == "__main__":
    unittest.main()
