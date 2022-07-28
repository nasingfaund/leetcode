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
        
class Solution:

    def canPartition(self, nums):
        memo = {}
        def _can_partition(index, s):
            if (index, s) in memo:
                return memo[(index, s)]
            
            if s == 0:
                return True

            if index >= len(nums) or s < 0: # or if num[index] <= sum:
                return False
            memo[(index, s)] = _can_partition(index + 1, s-nums[index]) or _can_partition(index + 1, s)
            return memo[(index, s)]
        
        total_sum = sum(nums)
        
        return total_sum & 1 == 0 and _can_partition(0, total_sum//2)
    
    
    
class Solution:
    def canPartition(self, nums):
        total_sum = sum(nums)

        if total_sum & 2 == 1:
            return False

        half_sum = total_sum // 2
        aset = {0}

        for num in nums:
            subset = set()
            for elem in aset:
                if (elem + num) == half_sum:
                    return True
                subset.add(elem + num)
            aset |= subset
        return half_sum in aset
    
# two dimensional DP        
class Solution:
    def canPartition(self, nums):
        total_sum = sum(nums)
        if total_sum & 1: return False
        
        half_sum = total_sum // 2
        
        dp = [[False]*len(range(half_sum + 1)) for _ in range(len(nums))]
        
        for i in range(len(dp)):
            dp[i][0] = True
            
        for i in range(len(nums)):
            for j in range(half_sum+1):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                    
        return dp[len(nums)-1][half_sum]
