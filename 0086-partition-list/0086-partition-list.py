# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None

        less_dummy, not_less_dummy = ListNode(), ListNode()
        less, not_less = less_dummy, not_less_dummy
        node = head
        
        while node:
            if node.val < x:
                less.next = node
                less = less.next
            else:
                not_less.next = node
                not_less = not_less.next
            
            node = node.next

        not_less.next = None
        less.next = not_less_dummy.next
        
        return less_dummy.next
        