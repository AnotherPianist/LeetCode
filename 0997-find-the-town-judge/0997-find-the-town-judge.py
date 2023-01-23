class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degrees = [0] * n
        
        for i, j in trust:
            degrees[i - 1] -= 1
            degrees[j - 1] += 1
        
        for i, degree in enumerate(degrees):
            if degree == n - 1:
                return i + 1
        
        return -1