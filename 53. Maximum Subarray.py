# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            best = max(best, curr_sum)
        return best
