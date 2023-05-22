class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def find_first_land():
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        return i, j
        
        def mark_first_island():
            i_start, j_start = find_first_land()
            grid[i_start][j_start] = 2
            queue = deque([(i_start, j_start)])
            first_island_nodes = deque([(i_start, j_start)])
            
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()

                    for _i, _j in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                        if 0 <= _i < n and 0 <= _j < n and grid[_i][_j] == 1:
                            queue.append((_i, _j))
                            first_island_nodes.append((_i, _j))
                            grid[_i][_j] = 2

            return first_island_nodes
        
        def build_bridge(queue):
            distance = 0
            
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()

                    for _i, _j in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                        if 0 <= _i < n and 0 <= _j < n:
                            if grid[_i][_j] == 1:
                                return distance
                            elif grid[_i][_j] == 0:
                                queue.append((_i, _j))
                                grid[_i][_j] = -1

                distance += 1
                    
        
        return build_bridge(mark_first_island())