from typing import Union, Any, Tuple


class Heap:
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

    def build_push_down(self, index: int) -> list:
        # the correct intent of this code supposed to be:
        # if the  heap is empty, then swift up. Otherwise, swift down
        if self.heap:
            return self._build_push_down_heapify(index=index)
        else:
            return self._build_push_up_heapify(index=index)

    def _single_child(self, index: int) -> bool:
        return self.left_child(index) < len(self.heap) and self.right_child(
            index
        ) >= len(
            self.heap
        )  # pragma: no cover

    def _is_leaf(self, index: int) -> bool:
        return self.left_child(index) >= len(self.heap) and self.right_child(
            index
        ) >= len(
            self.heap
        )  # pragma: no cover

    def _build_push_down_heapify(self, index: int) -> list:
        if not self._is_leaf(index):  # pragma: no cover
            if not self._single_child(index):  # pragma: no cover
                left = self.left_child(index)
                right = self.right_child(index)

                # explicitly checks both children and parent
                if (
                    self.heap[left][1] >= self.heap[index][1]
                    and self.heap[right][1] >= self.heap[index][1]
                ):
                    return self.heap

                # fixed at v1.3.0: wrong child is being swapped which is caused
                # breaking the min-heap invariant. now it will be swapped
                # with the right child first and then recursively on right side
                if self.heap[left][1] <= self.heap[right][1]:
                    self.heap[left], self.heap[index] = (
                        self.heap[index],
                        self.heap[left],
                    )
                    self._build_push_down_heapify(left)
                else:
                    self.heap[right], self.heap[index] = (
                        self.heap[index],
                        self.heap[right],
                    )
                    self._build_push_down_heapify(right)
                return self.heap

            # single left child only
            left = self.left_child(index)
            if self.heap[left][1] >= self.heap[index][1]:
                pass
            else:
                self.heap[left], self.heap[index] = (self.heap[index], self.heap[left])
            return self.heap

        return self.heap

    @property
    def build_floyd_heap(self) -> list:
        """Build Min-Heap based on Floyd's linear-time heap construction algorithm."""
        # fixed at v1.3.0: heap object is iterates an over integer, not a list
        # causing `TypeError` immediately. the correct intent must be iterates
        # from backwards through all lists and then heapify the object from bottom
        for index in range(len(self.heap) // 2 - 1, -1, -1):
            self._build_push_down_heapify(index)
        return self.heap

    def _build_push_up_heapify(self, index: int) -> list:
        """Bubble up algorithm."""
        # fixed at v1.3.0: an old bug since 6 years ago which is silently
        # accessed heap object from the last element instead of skipping it
        if index <= 0:
            return self.heap

        parent = self.parent(index=index)
        if self.heap[parent][1] <= self.heap[index][1]:
            pass
        else:
            self.heap[parent], self.heap[index] = (
                self.heap[index],
                self.heap[parent],
            )
            self._build_push_up_heapify(parent)
        return self.heap

    def validate_heapify(self) -> bool:
        # fixed at v1.3.0: an old bug since 6 years ago, compare
        # the root of element against heap object instead of skipping it
        for index, element in enumerate(self.heap):
            if index > 0:
                if self.heap[self.parent(index)][1] > self.heap[index][1]:
                    return False
        return True

    def add(self, key: object, value: object) -> None:
        """Add and append the element in index."""
        self.heap.append((key, value))
        self._build_push_up_heapify(len(self.heap) - 1)

    def remove(self) -> None:
        """Remove minimum element in index."""
        # fixed at v1.3.0: correct approach should be swapped the root
        # with the last element, and then popped out that last element,
        # and then swift up the new root to restore the heap property
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        minimum = self.heap.pop()
        if self.heap:
            self._build_push_down_heapify(0)
        return minimum

    def update(self, key: object, value: object) -> list:
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

    def remove_key(self, key) -> list:
        """Remove element in index based on their key."""
        for index, element in enumerate(self.heap):  # pragma: no cover
            if element[0] == key:
                last_element = self.heap.pop()

                # if removed element was already the last element, we can just return the heap
                if index == len(self.heap):
                    return self.heap
                self.heap[index] = last_element

                # then we can restore the heap property in both ways
                self._build_push_down_heapify(index)
                self._build_push_up_heapify(index)
                return self.heap
        return self.heap
