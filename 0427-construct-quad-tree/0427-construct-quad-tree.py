"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def recursion(i, j, size):
            if size == 1:
                return Node(grid[i][j], True, None, None, None, None)
            
            size //= 2

            node = Node(
                grid[i][j],
                False,
                recursion(i, j, size),
                recursion(i, j +  size, size),
                recursion(i + size, j, size),
                recursion(i + size, j + size, size)
            )
                        
            if \
                node.topLeft.isLeaf and \
                node.topRight.isLeaf and \
                node.bottomLeft.isLeaf and \
                node.bottomRight.isLeaf and \
                node.topLeft.val == node.topRight.val == node.bottomLeft.val == node.bottomRight.val:
                return Node(node.val, True, None, None, None, None)
            return node
        
        return recursion(0, 0, len(grid))