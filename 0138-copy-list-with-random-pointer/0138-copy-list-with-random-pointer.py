"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visited = {}
    
    def clone_node(self, node):
        if not node:
            return None

        if node not in self.visited:
            self.visited[node] = Node(node.val, None, None)
        return self.visited[node]

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        node = head
        new_node = Node(node.val, None, None)
        self.visited[node] = new_node

        while node:
            new_node.random = self.clone_node(node.random)
            new_node.next = self.clone_node(node.next)
            node, new_node = node.next, new_node.next
        
        return self.visited[head]
