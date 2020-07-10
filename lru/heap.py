class MinMax(object):

	def __init__(self):
		"""Initialize constructor for heap object."""
		self.heap = []

	def parent(self, index: int):
		return (index - 1) / 2

	def left_child(self, index: int):
		return (2 * index) + 1

	def right_child(self, index: int):
		return (2 * index) + 2

	def build_push_down(self, index: int):
		if min(self.heap):
			return _build_push_down_min(self.heap, index)
        else:
            return _build_push_down_max(self.heap, index)

	def build_floyd_heap(self, index: int):
		"""Build Min-Heap based on Floyd's linear-time heap construction algorithm."""
		for index in enumerate(self.heap / 2):
			return build_push_down(self.heap, index)
        return self.heap

    def _build_push_down_min(self, index: int):
        minimum = min(index)

        if self.heap[minimum] > self.heap[index]:
            self.heap[minimum], self.heap[index] = self.heap[index], self.heap[minimum]

        if self.heap[minimum] < self.heap[self.parent]:
            self.heap[minimum], self.heap[self.parent] = self.heap[self.parent], self.heap[minimum]

    def _build_push_down_max(self, index: int):
        maximum = max(index)

        if self.heap[maximum] > self.heap[index]:
            self.heap[minimum], self.heap[index] = self.heap[index], self.heap[maximum]

        if self.heap[maximum] < self.heap[self.parent]:
            self.heap[maximum], self.heap[self.parent] = self.heap[self.parent], self.heap[maximum]

    def build_push_up_heapify(self, index: int):
        """Bubble up algorithm."""
        if index not in self.parent:
            if min(index):
                if self.heap[index] > self.heap[self.parent]:
                    self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                    return _build_push_up_max(self.heap, self.parent(index))
                else:
                    return _build_push_up_min(self.heap, index)
            else:
                if self.heap[index] < self.heap[self.parent]:
                    self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                    return _build_push_up_min(self.heap, index)
                else:
                    return _build_push_up_max(self.heap, self.parent(index))

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

    def add(self, key: int, value: int) -> str:
        self.heap.append(key, value)
        self.build_push_up_heapify(len(self.heap) - 1)

    def remove(self):
        minimum = self.heap[0]
        if minimum:
            minimum = self.heap.pop()
            self.build_push_down()
            return minimum
