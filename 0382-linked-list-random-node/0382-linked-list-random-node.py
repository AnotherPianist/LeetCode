from random import random


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    
    def getRandom(self) -> int:
        scope = 1
        reservoir = 0
        current = self.head
        
        while current:
            if random() < 1 / scope:
                reservoir = current.val
            current = current.next
            scope += 1
        
        return reservoir
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()