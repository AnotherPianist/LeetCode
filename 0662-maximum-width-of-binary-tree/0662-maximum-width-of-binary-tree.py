from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 1
        queue = deque([(root, 0)])
        
        while queue:
            start_index = queue[0][1]
            
            for _ in range(len(queue)):
                node, end_index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * end_index))
                if node.right:
                    queue.append((node.right, 2 * end_index + 1))
            
            max_width = max(max_width, end_index - start_index + 1)
        
        return max_width