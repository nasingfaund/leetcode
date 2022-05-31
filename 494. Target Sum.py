# TLE, how to improve? Time Complexity: O(2**n), Space Complexity: O(1)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = 0
        n = len(nums)
        for num in range(2**n):
            curr_sum = 0
            mask = bin(num)[2:].zfill(n)
            for i in range(n):
                if mask[i] == '1':
                    curr_sum += nums[i]
                else:
                    curr_sum -= nums[i]
            if curr_sum == target:
                result +=1
        return result
        
# Brute Force with memo Time Complexity: O(sum(nums)*len(nums)), Space Complexity: O(sum(nums) * len(nums)) 
class Solution:
    def findTargetSumWays(self, nums, target):
        @cache
        def _findTargetSumWays(sum, index) -> int:
            if index == len(nums):
                if sum == target:
                    return 1
                return 0

            first = _findTargetSumWays(sum + nums[index], index + 1)

            second = _findTargetSumWays(sum - nums[index], index + 1)

            return first + second
        
        return _findTargetSumWays(0, 0)
        
class Solution:
    def findTargetSumWays(self, nums, target):
        memo = {}
        def _findTargetSumWays(sum, index) -> int:
            if (sum, index) in memo:
                return memo[(sum, index)]
            
            if index == len(nums):
                if sum == target:
                    return 1
                return 0

            first = _findTargetSumWays(sum + nums[index], index + 1)

            second = _findTargetSumWays(sum - nums[index], index + 1)
            
            memo[(sum, index)]  = first + second
            return memo[(sum, index)]
        
        return _findTargetSumWays(0, 0)
    
class Solution:
    def findTargetSumWays(self, nums, target):
        count = defaultdict(int)
        count[0] = 1
        for x in nums:
            step = defaultdict(int)
            for y in count:
                step[y + x] += count[y]
                step[y - x] += count[y]
            count = step
        return count[target]

