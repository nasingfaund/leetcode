# Brute force: Time complexity O(2**(m*n)), Space complixity O(2**(m*n))
class Solution:
    def uniquePaths(self, m, n):
        def helper(m, n):
            elif m == 0 or n == 0: 
                return 1
            else:
                return helper(m-1, n) + helper(m, n-1)
        return helper(m-1, n-1)

# brute force with memoization, Time complexity O(m*n), Space complexity O(m*n)
class Solution:
    def uniquePaths(self, m, n):
        memo = {}
        def helper(m, n):
            if (m, n) in memo:
                return memo[(m, n)]
            elif m == 0 or n == 0: 
                return 1
            else:
                memo[(m, n)] = helper(m-1, n) + helper(m, n-1)
            return memo[(m, n)]
        
        return helper(m-1, n-1)
    

# Time complexity O(m*n), Space complexity O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1 for i in range(n)] for j in range(m)]
            
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
                
        return matrix[m-1][n-1]
    
# Optimization by space, no need to store m*n array, one row is enough
# Time complexity O(m*n), Space complexity O(n)
class Solution:
    def uniquePaths(m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]

# Time complexity O(m+n), Space complexity O(1)
class Solution:
    def uniquePaths(self, m, n):
        return factorial(m+n-2) // factorial(m-1) // factorial(n-1)
