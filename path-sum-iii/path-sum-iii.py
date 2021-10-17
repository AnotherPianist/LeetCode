# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        paths = 0
        cache = {0: 1}
        
        def dfs(node, currSum):
            nonlocal cache, paths
            if node:
                currSum += node.val
                oldSum = currSum - targetSum
                if oldSum in cache:
                    paths += cache[oldSum]
                cache[currSum] = cache.get(currSum, 0) + 1
                dfs(node.left, currSum)
                dfs(node.right, currSum)
                cache[currSum] -= 1
            
        dfs(root, 0)
        return paths