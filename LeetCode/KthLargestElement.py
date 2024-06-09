class MaxHeap:
    def __init__(self, k):
        self.k = k
        self.heap = []

    def add(self, num):
        if len(self.heap) < self.k:
            self.heap.append(num)
            self._bubble_up(len(self.heap) - 1)
        elif num < self.heap[0]:
            self.heap[0] = num
            self._bubble_down(0)
        return self.heap[0]

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._bubble_up(parent)

    def _bubble_down(self, index):
        largest = index
        left, right = 2 * index + 1, 2 * index + 2
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self._bubble_down(largest)

# Usage:
kthLargest = MaxHeap(3)
for num in [4, 5, 8, 2]:
    print(kthLargest.add(num))  # prints 4, 5, 5