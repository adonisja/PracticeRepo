class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    elif l2:
        current.next = l2

    return dummy.next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("/")


def main():
    # Test cases
    '''test_cases = [
        ([], []),
        ([1, 3, 5], []),
        ([], [2, 4, 6]),
        ([1, 3, 5], [2, 4, 6]),
        ([1, 2, 3], [4, 5]),
        ([1, 2, 2], [2, 3, 4]),
        ([-3, -1, 2], [-2, 0, 3]),
        ([1, 1, 1], [1, 1, 1])
    ]'''
    test_cases = [([], []),
    ([1, 3, 5], []),
    ([], [2, 4, 6]),
    ([1, 3, 5], [2, 4, 6]),
    ([1, 2, 3], [4, 5]),
    ([1, 2, 2], [2, 3, 4]),
    ([-3, -1, 2], [-2, 0, 3]),
    ([1, 1, 1], [1, 1, 1]),
    ([1, 4, 5], [2, 3, 6]),
    ([1, 2, 4], [1, 3, 4]),
    ([5, 10, 15], [2, 3, 20]),
    ([1, 2, 3], [7, 8, 9]),
    ([1, 3, 5, 7], [2, 4, 6, 8]),
    ([1, 2, 3, 4], [5, 6, 7, 8]),
    ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]),
    ([1], [2]),
    ([2], [1]),
    ([1, 2, 3], [1, 2, 3])
    ]

    for i, (l1_values, l2_values) in enumerate(test_cases):
        l1 = create_linked_list(l1_values)
        l2 = create_linked_list(l2_values)
        print(f"Test {i + 1}:")
        print("l1: ", end="")
        print_linked_list(l1)
        print("l2: ", end="")
        print_linked_list(l2)
        merged_list = mergeTwoLists(l1, l2)
        print("Merged: ", end="")
        print_linked_list(merged_list)
        print()

if __name__ == '__main__':
    main()