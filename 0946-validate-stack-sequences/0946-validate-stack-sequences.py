class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        
        for val in pushed:
            stack.append(val)
            while stack and i < len(popped) and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        
        return i == len(popped)