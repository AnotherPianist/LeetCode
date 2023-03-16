# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.post_idx = len(postorder) - 1
        m = {val: i for i, val in enumerate(inorder)}
        
        def build(start, end):
            if start > end:
                return None
            root = TreeNode(postorder[self.post_idx])
            self.post_idx -= 1
            
            root.right = build(m[root.val] + 1, end)
            root.left = build(start, m[root.val] - 1)
            
            return root
        
        return build(0, len(inorder) - 1)