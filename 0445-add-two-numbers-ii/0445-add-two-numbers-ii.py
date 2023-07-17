# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack_1, stack_2 = [], []
        
        while l1:
            stack_1.append(l1.val)
            l1 = l1.next
        while l2:
            stack_2.append(l2.val)
            l2 = l2.next
        
        total = carry = 0
        node = ListNode()
        
        while stack_1 or stack_2:
            if stack_1:
                total += stack_1.pop()
            if stack_2:
                total += stack_2.pop()
            
            node.val = total % 10
            carry = total // 10
            
            node = ListNode(carry, node)
            total = carry
        
        return node.next if carry == 0 else node