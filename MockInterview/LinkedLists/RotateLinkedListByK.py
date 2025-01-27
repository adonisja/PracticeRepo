class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

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

def RotateByK(head, k):
    #Check if the LL is empty
    if not head:
        return head
    length, tail = 1, head

    #move tail to the end of the LL
    while tail.next:
        tail = tail.next
        length += 1
    '''If k is greater than the length of the LL, then we should
    divide by the length and rotate by the remainder to do this,
    we use mod on all k values to get the appropriate value'''
    print(f'length: {length}')
    k = k % length
    if k == 0:
        return head
    
    #Current will keep track of the pivot
    current = head
    for i in range(length - k - 1):
        current = current.next
    
    '''Set the temp node(new head) to the pivot, and make the pivot
    the head of the LL, then connect the tail to the previous head
    of the LL''' 
    newHead = current.next
    current.next = None
    tail.next = head

    #return the new head
    return newHead

def test_rotateLinkedListByK():
    test_cases = [
        ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 1, [5, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 7, [4, 5, 1, 2, 3]),
        ([], 3, []),
        ([1], 2, [1]),
        ([-1, -2, -3, -4, -5], 3, [-3, -4, -5, -1, -2])
    ]

    for i, (values, k, expected) in enumerate(test_cases):
        head = create_linked_list(values)
        
        print(f"Test {i + 1}:")
        print(f'k = {k}')
        print("Original: ", end="")
        print_linked_list(head)
        if not head: 
            print(f'length = 0')
        rotated_head = RotateByK(head, k)
        print("Rotated:  ", end="")
        print_linked_list(rotated_head)
        print()

if __name__ == '__main__':
    test_rotateLinkedListByK()
        
