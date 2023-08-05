# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}

        def allPossibleBST(start, end):
            trees = []
            if start > end:
                trees.append(None)
                return trees

            if (start, end) in memo:
                return memo[(start, end)]

            for i in range(start, end + 1):
                leftSubTrees = allPossibleBST(start, i - 1)
                rightSubTrees = allPossibleBST(i + 1, end)

                for left in leftSubTrees:
                    for right in rightSubTrees:
                        root = TreeNode(i, left, right)
                        trees.append(root)

            memo[(start, end)] = trees
            return trees
        
        return allPossibleBST(1, n)