class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                                 
        if len(queue) == n**2 or len(queue) == 0: 
            return -1
        
        visited = set()
        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()

                for x, y in directions:
                    new_i = i + x
                    new_j = j + y

                    if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] == 0:
                        if not (new_i, new_j) in visited:
                            queue.append((new_i, new_j))
                            visited.add((new_i, new_j))
            level +=1
        return level - 1
                    
