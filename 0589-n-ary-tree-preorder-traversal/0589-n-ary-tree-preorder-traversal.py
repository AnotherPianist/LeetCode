"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack, res = [root], []
        
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.extend(reversed(node.children))
        return res