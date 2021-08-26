# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode(-1)
        sentinel.next = head
        fast = sentinel
        while n >= 0:
            fast = fast.next
            n -= 1
        slow = sentinel
        while fast:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next if slow.next else None
        return sentinel.next