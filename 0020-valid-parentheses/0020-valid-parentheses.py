class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {'(': ')', '{': '}', '[': ']'}
        
        for char in s:
            if char in m:
                stack.append(m[char])
            else:
                if not stack or stack[-1] != char:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0