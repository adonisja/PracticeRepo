import random

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def createLinkedList(values, pos):
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
    if pos != -1:
        current.next = nodes[pos]
    return head

def hasCycle(head):
    if not head:
        return False
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

def main():
    values = [3, 2, 0, -4]
    pos = random.choice(range(-1,len(values)))  # The position where the cycle starts (0-indexed), -1 means no cycle

    # Create linked list
    head = createLinkedList(values, pos)

    # Check for cycle
    result = hasCycle(head)
    print(f'Cycle detected: {result}')

if __name__ == '__main__':
    main()