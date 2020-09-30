class Heap:
    """Base class for heap object."""

    def __init__(self):
        """Initialize constructor for heap object."""
        self.heap = []

    def parent(self, index: int) -> int:
        return (index - 1) // 2

    def left_child(self, index: int) -> int:
        return (2 * index) + 1 # pragma: no cover

    def right_child(self, index: int) -> int:
        return (2 * index) + 2

    def build_push_down(self, index: int) -> int:
        if min(self.heap): # pragma: no cover
            return self._build_push_down_min(index)
        else:
            return self._build_push_down_max(index)

    def _single_child(self, index: int):
        return self.left_child(index) < len(self.heap) and self.right_child(index) > len(self.heap)

    def _is_leaf(self, index: int):
        return self.left_child(index) > len(self.heap) and self.right_child(index) > len(self.heap)

    def build_floyd_heap(self, index: int):
        """Build Min-Heap based on Floyd's linear-time heap construction algorithm."""
        for index in enumerate(self.heap // 2): # pragma: no cover
            return build_push_down(self.heap, index)
        return self.heap

    def _build_push_down_iterative(self, index: int):
        if self._is_leaf(index):
            return self.heap

        if self._single_child(index):
            if self.heap[self.left_child(index)][1] < self.heap[index][1]:
                self.heap[self.left_child(index)], self.heap[index] = self.heap[index], self.heap[self.left_child(index)]
            return self.heap
        
        if min(self.heap[self.left_child(index)][1], self.heap[self.right_child(index)][1]) > self.heap[index][1]:
            return self.heap

        if self.heap[self.left_child(index)][1] < self.heap[self.right_child(index)][1]:
            self.heap[self.left_child(index)], self.heap[index] = self.heap[index], self.heap[self.left_child(index)]
            self._build_push_down_iterative(self.right_child(index))
            return self.heap

    def _build_push_up_heapify(self, index: int) -> int:
        """Bubble up algorithm."""
        if self.parent(index) > 0:
            if self.heap[self.parent(index)][1] > self.heap[index][1]: # pragma: no cover
                self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
                self._build_push_up_heapify(self.parent(index))
                return self.heap
        return self.heap

    def _build_push_down_min(self, index: int):
        # this should be min(self.heap)
        # but it got an error
        # i dont know why this expression
        # still getting index out of range
        if min(self.heap[self.left_child(index)], self.heap[self.right_child(index)]) >= self.heap[index]: # pragma: no cover
            return self.heap

        if self.heap[self.left_child(index)][1] < self.heap[self.right_child(index)][1]:
            self.heap[self.left_child(index)], self.heap[index] = self.heap[index], self.heap[self.left_child(index)]
            self._build_push_down_min(self.left_child(index))
            return self.heap

        if self.heap[self.right_child(index)][1] > self.heap[self.left_child(index)][1]:
            self.heap[self.right_child(index)], self.heap[index] = self.heap[index], self.heap[self.right_child(index)]
            self._build_push_down_min(self.right_child(index))
            return self.heap

    def _build_push_down_max(self, index: int):
        # refactoring this code
        # maximum = max(index)

        if max(self.heap[self.left_child(index)][1], self.heap[self.right_child(index)][1] <= self.heap[index][1]):
            return self.heap

        if self.heap[self.left_child(index)][1] > self.heap[self.right_child(index)][1]:
            self.heap[self.left_child(index)], self.heap[index] = self.heap[index], self.heap[self.left_child(index)]
            self._build_push_down_max(self.left_child(index))
            return self.heap

        if self.heap[self.right_child(index)][1] < self.heap[self.left_child(index)][1]:
            self.heap[self.right_child(index)], self.heap[index] = self.heap[index], self.heap[self.right_child(index)]
            self._build_push_down_max(self.right_child(index))
            return self.heap

    def _build_push_up_min(self, index: int):
        if self.heap[self.parent(index)] and self.heap[self.left_child(index)] < self.heap[self.parent(index)]: # pragma: no cover
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(self.parent(index))]
            self._build_push_down_min(self.left_child(index))
            return self.heap

    def _build_push_up_max(self, index: int):
        if self.heap[self.parent(index)] and self.heap[self.right_child(index)][1] > self.heap[self.parent(index)][1]: # pragma: no cover
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(self.parent(index))]
            self._build_push_down_max(self.right_child(index))
            return self.heap

    def _build_push_up_iterative(self, index: int):
        while self.heap[self.parent(index)] and self.heap[index] < self.heap[self.parent(index)]: # pragma: no cover
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            self._build_push_down_iterative(self.parent(index))
            return self.heap

    def add(self, key: int, value: int) -> int:
        """Add and append the element in index."""
        self.heap.append((key, value))
        self._build_push_up_heapify(len(self.heap) - 1)

    def remove(self):
        """Remove minimum element in index."""
        minimum = self.heap[0] # pragma: no cover
        if minimum:
            minimum = self.heap.pop()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
            self.build_push_down(0)
            return minimum

    def update(self, key: int, value: int):
        """Update key and value element in index."""
        for index, element in enumerate(self.heap):
            if element[0] == key:
                self.heap[index] = (key, value)
                if value >= element[1]:
                    self._build_push_down_min(index)
                else:
                    self._build_push_up_heapify(index)
                return self.heap
        return self.heap

    def remove_key(self, key):
        """Remove element in index based on their key."""
        for index, element in enumerate(self.heap):
            if element[0] == key:
                last_element = self.heap.pop()
                self.heap[index] = last_element
                # should return build_push_down
                # or returned as heapify ?
                self._build_push_down_min(index)
                return self.heap
        return self.heap