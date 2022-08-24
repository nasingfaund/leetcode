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
