# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        sums = []
        
        def dfs(node, formed):
            formed += str(node.val)
            if not node.left and not node.right:
                sums.append(int(formed))
            if node.left:
                dfs(node.left, formed)
            if node.right:
                dfs(node.right, formed)
            
        dfs(root, "")
        print(sums)
        return sum(sums)