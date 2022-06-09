class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid) # rows
        n = len(grid[0]) # cols
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque()
        level = 0
        zeroes = 0
        ones = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 0:
                    zeroes +=1
                elif grid[i][j] == 1:
                    ones += 1
        if not queue:
            if zeroes and not ones:
                return 0
            if ones and not zeroes:
                return -1
            return -1
                    
        while queue:
            for _ in range(len(queue)):
                
                i, j = queue.popleft()

                for x, y in directions:
                    new_i = i + x
                    new_j = j + y

                    if 0<= new_i < m and 0<= new_j < n and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        queue.append((new_i, new_j))
            level += 1
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                
        return level - 1
