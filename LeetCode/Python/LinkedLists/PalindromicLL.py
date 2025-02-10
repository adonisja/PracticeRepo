def isPalindrome(self, head: Optional[ListNode]) -> bool:
    LLArray = []
    if not head:
        return False
    temp = head
#        while temp:
#            LLArray.append(temp.val)
#            temp = temp.next
#        return LLArray[:] == LLArray[::-1]
    slow = head = fast
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # here, slow is the middle of the LL and fast is at the end
    # so now reverse the second half
    curr = slow
    prev = None
    next = curr.next
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    ptr1 = head
    ptr2 = prev
    while ptr1 and ptr2:
        if ptr1.val != ptr2.val:
            return False
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return True