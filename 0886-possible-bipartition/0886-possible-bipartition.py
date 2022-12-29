from collections import deque, defaultdict


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        neighbors = defaultdict(list)
        color = [None] * (n + 1)
        
        def bfs(source):
            q = deque([source])
            color[source] = 0
            
            while q:
                node = q.popleft()
                for neighbor in neighbors[node]:
                    if color[neighbor] == color[node]:
                        return False
                    if not color[neighbor]:
                        color[neighbor] = 0 if color[node] == 1 else 1
                        q.append(neighbor)
            return True
        
        for dislike in dislikes:
            neighbors[dislike[0]].append(dislike[1])
            neighbors[dislike[1]].append(dislike[0])
        
        for i in range(1, n + 1):
            if not color[i]:
                if not bfs(i):
                    return False
        
        return True