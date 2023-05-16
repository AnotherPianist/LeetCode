# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        node = dummy
        
        while node and node.next:
            prev_node, first_node, second_node = node, node.next, node.next.next
            
            if second_node:
                first_node.next = second_node.next
                prev_node.next = second_node
                second_node.next = first_node
            
            node = first_node
        
        return dummy.next