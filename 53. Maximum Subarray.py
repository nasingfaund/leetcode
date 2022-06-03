# Brute Force - O(n^2), Space Complexity: O(1) - TLE
class Solution:
    def maxSubArray(self, nums) -> int:
        best = 0
        for i in range(len(nums)):
            local_max = 0
            for j in range(i, len(nums)):
                local_max += nums[j]
                best = max(best, local_max)

    return best

# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            best = max(best, curr_sum)
        return best

# Recursive, Time Complexity: O(n), Time Complexity: O(n-for stack)
class Solution:
    def maxSubArray(self, nums) -> int:
        def find(index, curr_max):
            if index >= len(nums):
                return float('-inf')
            curr_max = max(nums[index], curr_max + nums[index])
            return max(curr_max,  find(index + 1, curr_max))
        return find(0, 0)
    
# Dynamic Programming - Tabulation
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)
            
# Memory Limit Exceeded
class Solution:
    def maxSubArray(self, nums) -> int:
        def find(index, curr_max):
            if index >= len(nums):
                return []
            curr_max = max(nums[index], curr_max + nums[index])
            return [curr_max] + find(index + 1, curr_max)

        return max(find(0, 0))

            
