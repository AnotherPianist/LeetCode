class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.res = 0

        def helper(start, indegree, count):
            if start == len(requests):
                for i in range(n):
                    if indegree[i] != 0:
                        return
                self.res = max(self.res, count)
                return

            indegree[requests[start][0]] -= 1
            indegree[requests[start][1]] += 1
            helper(start + 1, indegree, count + 1)

            indegree[requests[start][0]] += 1
            indegree[requests[start][1]] -= 1
            helper(start + 1, indegree, count)
        
        helper(0, [0] * n, 0)

        return self.res
