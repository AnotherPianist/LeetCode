from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        left_to_right = True
        res = []
        
        while queue:
            level = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val) if left_to_right else level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level)
            left_to_right = not left_to_right

        return res