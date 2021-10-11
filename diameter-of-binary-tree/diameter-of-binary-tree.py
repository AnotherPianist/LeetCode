# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return 0
        max_d = 0
        
        def search(node):
            nonlocal max_d
            if not node:
                return 0
            left = search(node.left)
            right = search(node.right)
            max_d = max(max_d, left + right)
            return 1 + (left if left >= right else right)
        
        search(root)
        return max_d