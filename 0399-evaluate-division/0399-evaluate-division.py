class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)

        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value
        
        results = []
        
        def dfs(current, target, cumulative_product):
            visited.add(current)
            res = -1.0
            
            if target in graph[current]:
                res = cumulative_product * graph[current][target]
            else:
                for neighbor, value in graph[current].items():
                    if neighbor in visited:
                        continue
                    res = dfs(neighbor, target, cumulative_product * value)
                    if res != -1.0:
                        break
            visited.remove(current)
            return res
        

        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                results.append(-1.0)
            elif dividend == divisor:
                results.append(1.0)
            else:
                visited = set()
                results.append(dfs(dividend, divisor, 1))
                
        return results