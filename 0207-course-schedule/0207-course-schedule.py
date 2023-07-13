from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            in_degree[prerequisite[0]] += 1
        
        queue = deque()
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        nodes_visited = 0
        
        while queue:
            node = queue.popleft()
            nodes_visited += 1
            
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return nodes_visited == numCourses