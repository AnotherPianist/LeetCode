class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        n, m = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] = 1
        
        for j in range(1, m):
            obstacleGrid[0][j] = obstacleGrid[0][j - 1] if obstacleGrid[0][j] == 0 else 0
        
        for i in range(1, n):
            obstacleGrid[i][0] = obstacleGrid[i - 1][0] if obstacleGrid[i][0] == 0 else 0
        
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0
        
        return obstacleGrid[-1][-1]