"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        m = {}
        node = head
        while node:
            m[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            m[node].next = m.get(node.next, None)
            m[node].random = m.get(node.random, None)
            node = node.next
        return m[head]