from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:        
        start_row, start_col = entrance
        maze[start_row][start_col] = "+"
        

        queue = deque()
        queue.append([start_row, start_col, 0])
        
        while queue:
            curr_row, curr_col, curr_distance = queue.popleft()
            
            for _i, _j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                next_row = curr_row + _i
                next_col = curr_col + _j
                
                if 0 <= next_row < len(maze) and 0 <= next_col < len(maze[0]) \
                    and maze[next_row][next_col] == ".":
                    
                    if 0 == next_row or next_row == len(maze) - 1 or 0 == next_col or next_col == len(maze[0]) - 1:
                        return curr_distance + 1
                    
                    maze[next_row][next_col] = "+"
                    queue.append([next_row, next_col, curr_distance + 1])
            
        return -1