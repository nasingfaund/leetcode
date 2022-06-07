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
            
            
