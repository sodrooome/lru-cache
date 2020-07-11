class Heap:
    """Base class for heap object."""

    def __init__(self):
        """Initialize constructor for heap object."""
        self.heap = []

    def parent(self, index: int) -> int:
        return (index - 1) // 2

    def left_child(self, index: int):
        return 2 * index + 1

    def right_child(self, index: int):
        return 2 * index + 2

    def build_push_down(self, index: int):
        if min(self.heap):
            return self._build_push_down_min(index)
        else:
            return self._build_push_down_max(index)

    def build_floyd_heap(self, index: int):
        """Build Min-Heap based on Floyd's linear-time heap construction algorithm."""
        for index in enumerate(self.heap // 2):
            return build_push_down(self.heap, index)
        return self.heap

    def _build_push_down_iterative(self, index: int):
        minimum = min(index)
        
        if minimum:
            if self.heap[minimum] > self.heap[index]:
                self.heap[minimum], self.heap[index] = self.heap[index], self.heap[minimum]
                if self.heap[minimum] < self.heap[self.parent]:
                    self.heap[minimum], self.heap[self.parent] = self.heap[self.parent], self.heap[minimum]
                    return _build_push_down_max(self.index, minimum)
        elif self.heap[minimum] < self.heap[index]:
            self.heap[minimum], self.heap[index] = self.heap[index], self.heap[minimum]

    def _build_push_up_heapify(self, index: int) -> int:
        """Bubble up algorithm."""
        if self.parent(index) > 0:
            if self.heap[self.parent(index)][1] > self.heap[index][1]:
                self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
                self._build_push_up_heapify(self.parent(index))
                return self.heap
        return self.heap

    def _build_push_down_min(self, index: int):
        # this should be min(self.heap)
        # but it got an error
        if self.heap[self.left_child(index)][1] > self.heap[index][1]:
            return self.heap

        if self.heap[self.left_child(index)][1] < self.heap[self.right_child(index)][1]:
            self.heap[self.left_child(index)], self.heap[i] = self.heap[index], self.heap[self.left_child(index)]
            self._build_push_down_min(self.left_child(index))
            return self.heap

        self.heap[self.right_child(i)], self.heap[index] = self.heap[index], self.heap[self.right_child(index)]
        self._build_push_down_min(self.right_child(index))
        return self.heap

    def _build_push_down_max(self, index: int):
        maximum = max(index)

        if self.heap[maximum] > self.heap[index]:
            self.heap[minimum], self.heap[index] = self.heap[index], self.heap[maximum]

        if self.heap[maximum] < self.heap[self.parent]:
            self.heap[maximum], self.heap[self.parent] = self.heap[self.parent], self.heap[maximum]    

    def _build_push_up_min(self, index: int):
        if index[self.parent] and self.heap[index] < self.heap[self.parent]:
            self.heap[index], self.heap[self.parent] = self.heap[self.parent], self.heap[index]
            return _build_push_up_min(self.heap, self.parent(index))

    def _build_push_up_max(self, index: int):
        if index[self.parent] and self.heap[index] > self.heap[self.parent]:
            self.heap[index], self.heap[self.parent] = self.heap[self.parent], self.heap[index]
            return _build_push_up_max(self.heap, self.parent(index))

    def _build_push_up_iterative(self, index: int):
        while index[self.parent] and self.heap[index] < self.heap[self.parent]:
            self.heap[index], self.heap[self.parent] = self.heap[self.parent], self.heap[index]
            index = self.parent(index)

    def add(self, key: int, value: int) -> int:
        self.heap.append((key, value))
        self._build_push_up_heapify(len(self.heap) - 1)

    def remove(self):
        """Remove minimum element in index."""
        minimum = self.heap[0]
        if minimum:
            minimum = self.heap.pop()
            self.build_push_down(0)
            return minimum

    def update(self, key: int, value: int):
        for index, element in enumerate(self.heap):
            if element[0] == key:
                self.heap[key] = (key, value)
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
                self.heap[i] = last_element
                self.build_push_down()
                return self.heap
        return self.heap