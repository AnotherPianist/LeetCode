class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p1, p2, p3):
            return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
        
        def construct_half_hull(points):
            stack = []
            for p in points:
                while len(stack) >= 2 and cross(stack[-2], stack[-1], p) > 0:
                    stack.pop()
                stack.append(tuple(p))
            return stack
        
        trees.sort()
        left_to_right = construct_half_hull(trees)
        right_to_left = construct_half_hull(reversed(trees))
        
        return set(left_to_right + right_to_left)