from collections import deque
# tle
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        n = len(mat)
        m = len(mat[0])
        dist = [[float('inf')]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))
        
        while queue:
            i, j = queue.pop()
            
            if i + 1 < n and dist[i+1][j] > dist[i][j] + 1:
                dist[i+1][j] = dist[i][j] + 1
                queue.append((i+1, j))
            
            if j + 1<m and dist[i][j+1] > dist[i][j] +1:
                dist[i][j+1] = dist[i][j] + 1
                queue.append((i, j+1))
                
            if i - 1 >=0 and dist[i-1][j] > dist[i][j] + 1:
                dist[i-1][j] = dist[i][j] +1
                queue.append((i-1, j))
                
            if j-1>=0 and dist[i][j-1] > dist[i][j] + 1:
                dist[i][j-1] = dist[i][j] + 1
                queue.append((i, j-1))
        return dist
            
            
            
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        queue = deque()
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1  # Marked as not processed yet!

        while queue:
            i, j = queue.popleft()
            for x, y in directions:
                nr = i + x
                nc = j + y
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[i][j] + 1
                    queue.append((nr, nc))
        return mat
