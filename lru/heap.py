from typing import Union, Any, Tuple


class Heap(object):
    """Base class for heap object."""

    def __init__(self, cache_list=None):
        """Initialize constructor for heap object."""
        if cache_list is None:
            cache_list = []
        self.heap = []
        if len(cache_list) > 0:
            for element in cache_list:
                self.add(element[0], element[1])

    def parent(self, index: int) -> int:
        return (index - 1) // 2  # pragma: no cover

    def left_child(self, index: int) -> int:
        return (2 * index) + 1  # pragma: no cover

    def right_child(self, index: int) -> int:
        return (2 * index) + 2  # pragma: no cover

    def build_push_down(self, index: int) -> Union[list, int]:
        if min(self.heap):  # pragma: no cover
            return self._build_push_down_heapify(index)
        else:
            return self._build_push_up_heapify(index)

    def _single_child(self, index: int):
        return self.left_child(index) < len(self.heap) and self.right_child(index) >= len(
            self.heap)  # pragma: no cover

    def _is_leaf(self, index: int):
        return self.left_child(index) >= len(self.heap) and self.right_child(index) >= len(
            self.heap)  # pragma: no cover

    def _build_push_down_heapify(self, index: int):
        if not self._is_leaf(index):  # pragma: no cover
            if not self._single_child(index):  # pragma: no cover
                if min(self.heap[self.left_child(index)][1], self.heap[self.right_child(index)][1]) >= \
                    self.heap[index][
                        1]:  # pragma: no cover
                    return self.heap

                if self.heap[self.left_child(index)][1] >= self.heap[self.right_child(index)][1]:  # pragma: no cover
                    return
                self.heap[self.left_child(index)], self.heap[index] = self.heap[index], self.heap[
                    self.left_child(index)]
                self._build_push_down_heapify(self.right_child(index))
                return self.heap

            if self.heap[self.left_child(index)][1] >= self.heap[index][1]:
                pass
            else:
                self.heap[self.left_child(index)], self.heap[index] = self.heap[index], self.heap[
                    self.left_child(index)]
            return self.heap

        return self.heap

    @property
    def build_floyd_heap(self):
        """Build Min-Heap based on Floyd's linear-time heap construction algorithm."""
        index: Union[Tuple[int, Any], Any]
        for _ in enumerate(self.heap // 2):  # pragma: no cover
            return self._build_push_down_heapify(self.heap)
        return self.heap

    def _build_push_up_heapify(self, index: int) -> list:
        """Bubble up algorithm."""
        if self.parent(index) < 0:
            pass
        else:
            if self.heap[self.parent(index)][1] <= self.heap[index][1]:
                pass
            else:  # pragma: no cover
                self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
                self._build_push_up_heapify(self.parent(index))
                return self.heap
        return self.heap

    def validate_heapify(self):
        # WIP: fix this method
        for index, element in enumerate(self.heap):
            if self.parent(index) >= 0:
                if self.heap[self.parent(index)][1] > self.heap[index][1]:
                    print(self.heap[self.parent(index)], self.heap[index])
                    return False
        return True

    def add(self, key: object, value: object) -> object:
        """Add and append the element in index."""
        self.heap.append((key, value))
        self._build_push_up_heapify(len(self.heap) - 1)

    def remove(self):
        """Remove minimum element in index."""
        minimum = self.heap[0]  # pragma: no cover
        if minimum:
            minimum = self.heap.pop()
            self._build_push_down_heapify(0)
            return minimum

    def update(self, key: object, value: object) -> object:
        """Update key and value element in index."""
        for index, element in enumerate(self.heap):
            if element[0] == key:
                self.heap[index] = (key, value)
                if value > element[1]:
                    self._build_push_down_heapify(index)
                else:
                    self._build_push_up_heapify(index)
                return self.heap
        return self.heap

    def remove_key(self, key):
        """Remove element in index based on their key."""
        for index, element in enumerate(self.heap):  # pragma: no cover
            if element[0] == key:
                last_element = self.heap.pop()
                self.heap[index] = last_element
                self._build_push_down_heapify(index)
                return self.heap
        return self.heap
