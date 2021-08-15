# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        sentinel = ListNode(None)
        curr = sentinel
        c = 0
        while l1 and l2:
            s = l1.val + l2.val + c
            if s > 9:
                c = 1
                s -= 10
            else:
                c = 0
            curr.next = ListNode(s)
            curr, l1, l2 = curr.next, l1.next, l2.next
        l = None
        if l1:
            l = l1
        elif l2:
            l = l2
        while l:
            s = l.val + c
            if s > 9:
                c = 1
                s -= 10
            else:
                c = 0
            curr.next = ListNode(s)
            curr = curr.next
            l = l.next
        if c == 1:
            curr.next = ListNode(1)
        return sentinel.next