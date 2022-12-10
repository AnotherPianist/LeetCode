# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total, self.res = 0, float('-inf')
        
        def subtree_sum(node):
            if not node:
                return 0
            s = node.val + subtree_sum(node.left) + subtree_sum(node.right)
            self.res = max(self.res, (total - s) * s)
            return s
        
        total = subtree_sum(root)
        subtree_sum(root)
        return self.res % (10 ** 9 + 7)