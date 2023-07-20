class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and 0 < stack[-1] < abs(asteroid):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack and stack[-1] == abs(asteroid):
                    stack.pop()
        
        return stack