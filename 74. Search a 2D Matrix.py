class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m  = len(matrix) # rows
        n = len(matrix[0]) # cols
        
        first = 0
        second = n * m - 1
        
        while first <= second:
            middle = first + (second  - first)//2
            
            if matrix[middle//n][middle%n] == target:
                return True
            if target > matrix[middle//n][middle % n]:
                first += 1
            else:
                second -=1
        return False
        

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m  = len(matrix) # rows
        n = len(matrix[0]) # cols
        row = None
        for i in range(m):
            if matrix[i][0]<= target <= matrix[i][-1]:
                row = i
                break
                
        if row is None:
            return False
        alist = matrix[row]
        
        first = 0
        second = len(alist) - 1
        while first <=second:
            middle = (first + second) // 2
            if target == alist[middle]:
                return True
            if target > alist[middle]:
                first= middle + 1
            else:
                second = middle -1
        return False
