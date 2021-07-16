class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m-1, -1, -1):
            for j in range(n):
                if matrix[i][j] > target:
                    break
                elif matrix[i][j] == target:
                    return True
        return False
                
                
        
