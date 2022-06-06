class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def find(image, i, j, newColor, oldColor):
            if i >= len(image) or j >= len(image[0]) or i < 0 or j < 0:
                return
            if image[i][j] != oldColor:
                return
            if image[i][j] == oldColor:
                image[i][j] = newColor

            find(image, i + 1, j, newColor, oldColor)
            find(image, i, j + 1, newColor, oldColor)
            find(image, i - 1, j, newColor, oldColor)
            find(image, i, j - 1, newColor, oldColor)
            return image
        
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        return find(image, sr, sc, newColor, oldColor)

      
      
      
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        
        stack = [(sr, sc)]
        n = len(image)
        m = len(image[0])
        while stack:
            i, j = stack.pop()
            
            if image[i][j] == oldColor:
                image[i][j] = newColor
            
            if i+1 <= n-1 and image[i+1][j] == oldColor:
                stack.append((i+1, j))
            if j+1 <= m-1 and image[i][j+1] == oldColor:
                stack.append((i, j+1))
            if  i-1 >=0 and image[i-1][j] == oldColor:
                stack.append((i-1, j))
            if j-1 >= 0 and image[i][j-1] == oldColor:
                stack.append((i, j-1))
        return image
      
      
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        queue = deque([(sr, sc)])
        n = len(image)
        m = len(image[0])
        while queue:
            i, j = queue.popleft()

            if image[i][j] == oldColor:
                image[i][j] = newColor

            if i + 1 <= n - 1 and image[i + 1][j] == oldColor:
                queue.append((i + 1, j))
            if j + 1 <= m - 1 and image[i][j + 1] == oldColor:
                queue.append((i, j + 1))
            if i - 1 >= 0 and image[i - 1][j] == oldColor:
                queue.append((i - 1, j))
            if j - 1 >= 0 and image[i][j - 1] == oldColor:
                queue.append((i, j - 1))
        return image
