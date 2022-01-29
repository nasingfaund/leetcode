# Space Complexity O(n*m)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        coordinates = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    coordinates[i][j] = 1

        for i in range(m):
            for j in range(n):
                if coordinates[i][j] == 1:
                    for k in range(n):
                        matrix[i][k] = 0
                    # zeroing the column
                    for c in range(m):
                        matrix[c][j] = 0
                        
                        
# Improved
class Solution(object):
    def setZeroes(self, matrix):
        col0 = True
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            if matrix[i][0] == 0:
                col0 = False
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(rows - 1, -1, -1):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if not col0:
                matrix[i][0] = 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        col_has_zero = False
        row_has_zero = False
        for j in range(m):
            if matrix[0][j] == 0:
                row_has_zero = True
        for j in range(n):
            if matrix[j][0] == 0:
                col_has_zero = True

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[0][i] == 0:
                for j in range(n):
                    matrix[j][i] = 0

        for i in range(1, n):
            if matrix[i][0] == 0:
                for j in range(m):
                    matrix[i][j] = 0

        if row_has_zero:
            for j in range(m):
                matrix[0][j] = 0

        if col_has_zero:
            for j in range(n):
                matrix[j][0] = 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        indexes = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    indexes+=[(i, n) for n in range(m)]
                    indexes+=[(n, j) for n in range(n)]

        for i, j in indexes:
            matrix[i][j] = 0

        return matrix
