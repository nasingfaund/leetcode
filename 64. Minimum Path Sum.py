class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        @cache
        def find(i, j):
            if i == rows - 1 and j == cols - 1:
                return grid[i][j]
            if i ==  rows - 1:
                return grid[i][j] + find(i, j+1)
            if j == cols - 1:
                return grid[i][j] + find(i+1, j)
            
            if i>= rows or j >= cols:
                return 0
            return min(find(i+1, j), find(i, j + 1)) + grid[i][j]
        
        return find(0, 0)
        
