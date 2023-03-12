import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapq.heapify(h)
        
        dummy = ListNode()
        last = dummy
        
        while h:
            val, i, node = heapq.heappop(h)
            last.next, last = node, node
            
            if last.next:
                heapq.heappush(h, (last.next.val, i, last.next))
        
        return dummy.next