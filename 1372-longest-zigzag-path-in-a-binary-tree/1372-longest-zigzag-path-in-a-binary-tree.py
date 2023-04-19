# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        
        def zigzag(node, left, length):
            if node:
                self.max_length = max(self.max_length, length)
                if left:
                    zigzag(node.left, False, length + 1)
                    zigzag(node.right, True, 1)
                else:
                    zigzag(node.right, True, length + 1)
                    zigzag(node.left, False, 1)
            
        
        zigzag(root, True, 0)
        zigzag(root, False, 0)
        
        return self.max_length