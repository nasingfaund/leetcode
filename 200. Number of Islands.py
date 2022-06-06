class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid) # rows
        m = len(grid[0]) # col
        visited = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i >=n or j >= m or grid[i][j] == '0':
                return
            if (i, j) in visited:
                return 
            visited.add((i, j))
            dfs(i+1, j)
            dfs(i, j+1) 
            dfs(i-1, j) 
            dfs(i, j-1)
            
        result = 0
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == '1':
                    result += 1
                    dfs(i, j)
        return result
