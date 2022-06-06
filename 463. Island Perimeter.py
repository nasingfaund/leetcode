class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def find(i, j, visited):
            if i<0 or j <0 or i == n or j == m or grid[i][j] == 0:
                return 1
            
            if (i, j) in visited:
                return 0
            
            visited.add((i, j))
            
            return find(i+1, j, visited) + find(i, j+1, visited) + find(i-1, j, visited) + find(i, j-1, visited)
            
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return find(i, j, set())
        return 0       
