class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        alist = nums
        def solve(alist, index):
            if index in memo:
                return memo[index]
            if index >= len(alist):
                return 0
            best_with = alist[index] + solve(alist, index + 2)
            best_without = solve(alist, index + 1)

            memo[index] = max(best_with, best_without)

            return memo[index]
        return solve(alist, 0)
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        alist = nums
        if len(nums) == 0:
            return 0
        if len(alist) == 1:
            return alist[0]
        result = [0] * len(alist)
        
        result[1] = max(alist[0], alist[1])
        result[0] = alist[0]
        for i in range(2, len(alist)):
            result[i] = max(result[i - 1], result[i - 2] + alist[i])
        return result[-1]
