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
        def helper(target):
            if target == 0:
                return 1
            if target < 0:
                return
            res = 0
            for i in range(len(nums)):
                if target >= nums[i]:
                    res += helper(target - nums[i])
            return res
        
        return helper(target)
                
