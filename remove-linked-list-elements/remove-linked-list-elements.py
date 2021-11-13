# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        sentinel = ListNode(next=head)
        prev, node = sentinel, head
        while node:
            if node.val == val:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return sentinel.next