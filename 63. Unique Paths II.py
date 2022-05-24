class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        obstacleGrid[0][0] = 1

        for j in range(1, m):
            if obstacleGrid[j][0] != 1:
                obstacleGrid[j][0] = obstacleGrid[j-1][0]
            else:
                obstacleGrid[j][0] = 0
        
        for i in range(1, n):
            if obstacleGrid[0][i] != 1:
                obstacleGrid[0][i] = obstacleGrid[0][i - 1]
            else:
                obstacleGrid[0][i] = 0
                
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1]  + obstacleGrid[i - 1][j]
                else:
                    obstacleGrid[i][j] = 0
                
                
        return obstacleGrid[m-1][n-1]
