from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        triplet_to_id = {}
        count = defaultdict(int)
        res = []
        
        def traverse(node):
            if not node:
                return 0
            
            triplet = (traverse(node.left), node.val, traverse(node.right))
            
            if triplet not in triplet_to_id:
                triplet_to_id[triplet] = len(triplet_to_id) + 1
            
            id = triplet_to_id[triplet]
            count[id] += 1
            
            if count[id] == 2:
                res.append(node)

            return id


        traverse(root)

        return res