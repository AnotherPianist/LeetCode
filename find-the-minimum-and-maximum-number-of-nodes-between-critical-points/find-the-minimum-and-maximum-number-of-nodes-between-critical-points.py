# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next:
            return [-1, -1]
        criticals = []
        prev, node = head, head.next
        i = 1
        while node.next:
            if node.next and (prev.val < node.val and node.next.val < node.val) or (prev.val > node.val and node.next.val > node.val):
                criticals.append(i)
            prev, node = node, node.next
            i += 1
        if len(criticals) < 2:
            return [-1, -1]
        curr_min, curr_max = float('inf'), float('-inf')
        for i in range(len(criticals)):
            distance = abs(criticals[i] - criticals[i - 1])
            curr_min = min(distance, curr_min)
            curr_max = max(distance, curr_max)
        return [curr_min, curr_max]