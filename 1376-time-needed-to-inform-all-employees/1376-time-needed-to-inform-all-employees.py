from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        
        for i in range(n):
            if manager[i] != -1:
                graph[manager[i]].append(i)
        
        stack = [(headID, 0)]
        max_time = 0
        
        while stack:
            informant, prev_time = stack.pop()
            max_time = max(max_time, prev_time)
        
            for employee in graph[informant]:
                stack.append((employee, prev_time + informTime[informant]))
        
        return max_time