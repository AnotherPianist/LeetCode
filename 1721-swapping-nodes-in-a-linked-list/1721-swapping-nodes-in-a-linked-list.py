# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i = 0
        node = head
        
        while node:
            i += 1
            node = node.next
        
        size = i
        i = 0
        node = head
        
        while node:
            i += 1
            
            if i == k:
                first_node = node
            if i == size - k + 1:
                second_node = node
            
            node = node.next
        
        first_node.val, second_node.val = second_node.val, first_node.val
        
        return head