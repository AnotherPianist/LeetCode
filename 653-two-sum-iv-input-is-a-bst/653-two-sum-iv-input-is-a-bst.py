# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        
        def inorder(node):
            if not node:
                return False
            
            left = right = None
            
            if node.left:
                left = inorder(node.left)

            if k - node.val in s:
                return True
            s.add(node.val)

            if node.right:
                right = inorder(node.right)

            return left or right
        
        return inorder(root)