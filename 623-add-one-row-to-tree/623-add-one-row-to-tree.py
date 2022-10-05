# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        
        current_depth = 1
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if current_depth + 1 == depth:
                    new_node_left = TreeNode(val, node.left, None)
                    new_node_right = TreeNode(val, None, node.right)
                    node.left, node.right = new_node_left, new_node_right

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if current_depth + 1 == depth:
                return root
            
            current_depth += 1