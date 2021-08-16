# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd, even = head, head.next
        even_head = head.next
        while even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next
        odd.next = even_head
        return head