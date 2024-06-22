# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None): # This is a constructor
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):    
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = ListNode()  # This is a constructor
        self.head = head
        temp = fast = slow = head
        
        for count in range(n):  
 # This traverses the list to the nth node and moves the fast pointer to the nth node
            fast = fast.next
        while fast.next:        
            ''' This traverses the list to the end and moves the slow pointer 
            to the node before the nth node
            The logic is that the slow pointer will be at the node before the 
            nth node when the fast pointer is at the end of the list
            '''
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next # This removes the nth node by dereferencing it
        return temp.next # This returns the head of the list with the nth node removed
        
        