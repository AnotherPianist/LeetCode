class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        counts = [0] * len(string.ascii_lowercase)
        res = [0] * n
        
        def dfs(node, parent):
            i = ord(labels[node]) - ord('a')
            prev = counts[i]
            counts[i] += 1
            
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
            
            res[node] = counts[i] - prev
            
        dfs(0, -1)
        
        return res