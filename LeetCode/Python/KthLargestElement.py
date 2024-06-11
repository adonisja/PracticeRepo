# Problem: Kth Largest Element in a Stream
'''Implement KthLargest class:

KthLargest(int k, int[] nums): Initializes the object with the integer k and the stream of integers nums.
int add(int val): Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
💻 Reveal KthLargest Class Starter Code
Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8 '''

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.minHeap, self.k = nums, k # Initializing the minHeap and k
        heapq.heapify(self.minHeap)    # Converts the list into a heap
        while len(self.minHeap) > k: 
            ''' While the length of the heap is greater than k:
            This is done because there is never a need to keep 
            more than k elements in the heap.
            '''
            heapq.heappop(self.minHeap) 
            # Removes the smallest element from the heap

    def add(self, val):
        heapq.heappush(self.minHeap, val) # Adds the value to the heap
        if len(self.minHeap) > self.k: 
            # If the length of the heap is greater than k
            heapq.heappop(self.minHeap) 
            # Removes the smallest element from the heap
        return self.minHeap[0] # Returns the smallest element in the heap