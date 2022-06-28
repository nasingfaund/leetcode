# Time Complexity O(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    
# Time Complexity: O(2^n) - TLE
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def solve(i, prev):
            if i >= len(nums):
                return 0
            take = 0
            dontTake = solve(i+1, prev)
            if nums[i] > prev:
                take = 1 + solve(i +1, nums[i])

            return max(take, dontTake)

        return solve(0, float('-inf'))
