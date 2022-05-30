class Solution:

    def canPartition(self, nums):
        @cache
        def _can_partition(index, s):
            if s == 0:
                return True

            if index >= len(nums) or s < 0: # or if num[index] <= sum:
                return False

            return _can_partition(index + 1, s-nums[index]) or _can_partition(index + 1, s)
        
        total_sum = sum(nums)
        
        return total_sum & 1 == 0 and _can_partition(0, total_sum//2)
        
