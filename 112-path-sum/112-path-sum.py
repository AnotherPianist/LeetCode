# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return False if not root else self.dfs(root, 0, targetSum)
    
    def dfs(self, root, current_sum, target_sum):
        if not root.left and not root.right and current_sum + root.val == target_sum:
            return True
    
        left_result, right_result = False, False
        
        if root.left:
            left_result = self.dfs(root.left, current_sum + root.val, target_sum)
        if root.right:
            right_result = self.dfs(root.right, current_sum + root.val, target_sum)
        
        return left_result or right_result