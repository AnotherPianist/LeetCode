# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half_vals = []
        node = slow.next
        
        while node:
            second_half_vals.append(node.val)
            node = node.next
        
        node = head
        max_twin_sum = float('-inf')
        
        while second_half_vals:
            max_twin_sum = max(max_twin_sum, node.val + second_half_vals.pop())
            node = node.next
        
        return max_twin_sum