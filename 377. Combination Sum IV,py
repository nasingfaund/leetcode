class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target + 1)
        dp[0] = 1
        for j in range(1, target + 1):
            for i in range(len(nums)):
                if (j - nums[i]) >= 0:
                    dp[j] += dp[j - nums[i]]
        return dp[target]
            
        
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(target):
            if target == 0:
                return 1
            result = 0
            for num in nums:
                if target >= num:
                    result += dp(target-num)
                
            return result
        return dp(target)
            
