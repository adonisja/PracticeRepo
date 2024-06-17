'''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        tail = dummy
        temp1, temp2 = list1, list2

        while temp1 and temp2:
            if temp1.val <= temp2.val:
                tail.next = temp1
                temp1 = temp1.next
            else:
                tail.next = temp2
                temp2 = temp2.next
            tail = tail.next
        
        if temp1:
            tail.next = temp1
        if temp2:
            tail.next = temp2
        
        return dummy.next
    
def main():
    solution = Solution()
    list1 = [1,2,4]
    list2 = [1,3,4]
    solution.mergeTwoLists(list1, list2)

if __name__ == "__main__":
    main()

