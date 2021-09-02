# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def recursion(start, end):
            subtrees = []
            for root in range(start, end + 1):
                for left in recursion(start, root - 1):
                    for right in recursion(root + 1, end):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        subtrees.append(node)
            return subtrees if subtrees else [None]
        
        return recursion(1, n)