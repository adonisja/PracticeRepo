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

def middleNode(head):
    if not head:
        return None
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

def main():
    for test in testcases():
        nums, expected = test["nums"], test["expected"]
        head = createLinkedList(nums)
        result = middleNode(head)
        assert result == expected, f'Test case Array: {nums} Failed. Expected: {expected} but received: {result}'
    print(f'All Tests passed!')

def testcases():
    return[
       {"nums": [11, 2, 4, 5, 5 , 4, 3], "expected": 5},
        {"nums": [1], "expected": 1},
        {"nums": [], "expected": None},
        {"nums": [4, 9, 5, 6, 5, 3], "expected": 6}
    ]

if __name__ == '__main__':
    main()