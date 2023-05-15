# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        node = head
        first_node = second_node = None
        
        while node:
            length += 1
            
            if second_node:
                second_node = second_node.next
            if length == k:
                first_node = node
                second_node = head
            
            node = node.next
        
        first_node.val, second_node.val = second_node.val, first_node.val
        
        return head