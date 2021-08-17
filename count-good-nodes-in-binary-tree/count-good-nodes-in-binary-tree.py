# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return None
        
        def recursion(node, max_value):
            if not node:
                return 0
            max_value = max(node.val, max_value)
            return recursion(node.left, max_value) + recursion(node.right, max_value) + (node.val >= max_value)
        
        return recursion(root, root.val)