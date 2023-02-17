from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float("inf")
        self.prev_val = float("-inf")
        
        def inorder(node):
            if node.left:
                inorder(node.left)
            
            self.min_diff = min(self.min_diff, node.val - self.prev_val)
            self.prev_val = node.val
            
            if node.right:
                inorder(node.right)
        
        inorder(root)

        return self.min_diff