from collections import defaultdict


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        reachable_bombs = defaultdict(list)
        
        for i in range(n):
            for j in range(n):
                src_i, src_j, src_r = bombs[i]
                dst_i, dst_j, _ = bombs[j]
                
                if (dst_i - src_i) ** 2 + (dst_j - src_j) ** 2 <= src_r ** 2:
                    reachable_bombs[i].append(j)
        
        max_bombs = 0
        
        for start_bomb in range(n):
            stack = [start_bomb]
            visited = set(stack)
            
            while stack:
                current_bomb = stack.pop()
                
                for reachable_bomb in reachable_bombs[current_bomb]:
                    if reachable_bomb not in visited:
                        stack.append(reachable_bomb)
                        visited.add(reachable_bomb)
            
            max_bombs = max(max_bombs, len(visited))
        
        return max_bombs