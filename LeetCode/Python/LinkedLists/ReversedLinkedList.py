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

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    nodes = [head]
    for value in values[1:]:
        new_node = ListNode(value)
        current.next = new_node
        current = new_node
        nodes.append(new_node)
    return head

def LLtoList(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def reverseList(head):
    if not head:
        return None
    prev = None
    next = None
    current = head
    while(current): 
        next = current.next # This stores the next node
        current.next = prev # This reverses the link
        prev = current # This moves the prev pointer to the current node
        current = next # This moves the current pointer to the next node
    return prev   # This returns the head of the reversed list

def main():
    for test in testcases():
        nums, expected = test["nums"], test["expected"]
        head = createLinkedList(nums)
        resultLL = reverseList(head)
        result = LLtoList(resultLL)
        assert result == expected, f"Test case failed for Array: {nums}. Expected: {expected}, Result: {result}"
    print("All testcases passed!")

def testcases():
    return [
        {"nums": [1, 2, 3, 4, 5], "expected": [5, 4, 3, 2, 1]},
        {"nums": [1, 2], "expected": [2, 1]},
        {"nums": [], "expected": []},
        {"nums": [1], "expected": [1]},
    ]

if __name__ == '__main__':
    main()