from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        nodes = defaultdict(list)
        q = deque([(root, 0, 0)])
        while q:
            node, level, parent = q.popleft()
            nodes[node.val] = [level, parent]
            if node.left:
                q.append((node.left, level + 1, node.val))
            if node.right:
                q.append((node.right, level + 1, node.val))
        return nodes[x][0] == nodes[y][0] and nodes[x][1] != nodes[y][1]