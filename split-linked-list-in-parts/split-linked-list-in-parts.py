# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        res = []
        node = head
        for i in range(k):
            curr_head = node
            for _ in range(n // k + (i < n % k) - 1):
                if node:
                    node = node.next
            if node:
                node.next, node = None, node.next
            res.append(curr_head)
        return res