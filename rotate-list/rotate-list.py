# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        size = 1
        node = head
        while node.next:
            node = node.next
            size += 1
        node.next = head
        k = k % size
        node = head
        for _ in range(size - k - 1):
            node = node.next
        new_head = node.next
        node.next = None
        return new_head