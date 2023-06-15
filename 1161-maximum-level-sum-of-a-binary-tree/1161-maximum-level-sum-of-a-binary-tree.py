from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level_sum = root.val
        max_level_id = curr_level_id = 1
        
        queue = deque([root])
        
        while queue:
            curr_level_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                curr_level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if curr_level_sum > max_level_sum:
                max_level_sum = curr_level_sum
                max_level_id = curr_level_id
            
            curr_level_id += 1
        
        return max_level_id