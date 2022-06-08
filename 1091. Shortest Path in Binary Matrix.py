# Time Complexity BFS = O(V+ E), we have V = M*N and E = 8*V => O(V + 8*V) => O(9V) => O(M*N)
# Space complexty O(N*M)
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1]==1:
            return -1
        n  = len(grid)
        
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        
        queue = deque([(0, 0, 1)])
        visited = set()
        while queue:
            i, j, d = queue.popleft()
            
            if (i, j) == (n-1, n-1):
                return d
            
            for x, y in directions:
                new_i = i + x
                new_j = j + y
                
                if 0 <= new_i < n and 0<= new_j < n:
                    if (new_i, new_j) not in visited and grid[new_i][new_j] == 0:
                        queue.append((new_i, new_j, d+1))
                        visited.add((new_i, new_j))
        return -1
                
                    
        
        
        
        
        
