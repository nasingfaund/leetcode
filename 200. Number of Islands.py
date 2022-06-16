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
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)  # rows
        m = len(grid[0])  # col

        islands = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    islands.add((i, j))

        visited = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        count = 0
        for (i, j) in islands:
            if (i, j) in visited:
                continue
            count += 1
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                visited.add((i, j))
                for x, y in directions:
                    new_i = i + x
                    new_j = j + y
                    if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == "1":
                        if (new_i, new_j) not in visited:
                            stack.append((new_i, new_j))

        return count
