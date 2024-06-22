'''Given the head of a singly linked list, reverse the list, and return the reversed list.

Constraints
- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`
image of example 1
Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
image of example 2
Example 2:

Input: head = [1,2]
Output: [2,1]
Example 3:
Input: head = []
Output: []'''
class ListNode(object):
    def __init__(self, val=0, next=None): # This is a constructor
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        nextt = None
        current = head
        if current == None: # If the list is empty, return None
            return current
        while(current.next): 
            nextt = current.next # This stores the next node
            current.next = prev # This reverses the link
            prev = current # This moves the prev pointer to the current node
            current = nextt # This moves the current pointer to the next node
        current.next = prev # This reverses the link of the last node
        return current   # This returns the head of the reversed list