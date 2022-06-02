# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            best = max(best, curr_sum)
        return best

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)
            
