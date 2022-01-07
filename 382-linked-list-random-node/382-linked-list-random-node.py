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
        count = 1
        chosen_value = None
        curr = self.head
        
        while curr:
            if random() < 1 / count:
                chosen_value = curr.val
            curr = curr.next
            count += 1
        return chosen_value

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()