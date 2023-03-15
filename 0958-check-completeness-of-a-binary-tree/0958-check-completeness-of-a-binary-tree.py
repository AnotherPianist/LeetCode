from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([root])
        prev_node = root
        
        while queue:
            node = queue.popleft()
            
            if node:
                if not prev_node:
                    return False

                queue.append(node.left)
                queue.append(node.right)
            
            prev_node = node
        
        return True