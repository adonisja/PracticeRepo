class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.head = 0  # Initialzing the head pointer to 0
        self.tail = 0  # Initializing the tail pointer to 0
        self.k = k     # Storing the max size of the queue
        self.size = 0  # Storing the current size of the queue
        self.queue = [None] * k  
        ''' Initializing the queue with None values, 
        so that we can check if the queue is empty or not'''

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull(): # Checking if the queue is full
            return False
        self.queue[self.tail] = value # Adding the value to the tail pointer
        self.size += 1  # Increments the size of the queue
        self.tail = (self.tail + 1) % self.k # Moves the tail pointer to the next space
        return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty(): # Checks if the queue is empty
            print('The Queue is Empty, there is nothing to remove')
            return False
        self.queue[self.head] = None # Removes the value from the head pointer
        self.size -= 1  # Decrements the size of the queue
        self.head = (self.head + 1) % self.k 
        # Moves the head pointer to the next space
        return True
        

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty(): # Checks if the queue is empty
            print('The Queue is Empty, There is nothing to show!')
            return -1
        return self.queue[self.head] 
    # Returns the value at the head pointer

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            print('The Queue is Empty, There is nothing to show!')
            return -1
        return self.queue[self.tail - 1]
    # Returns the value at the tail pointer
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0 # Checks if the size of the queue is 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.k # Checks if the size of the queue is equal to the max size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()