# Time Limit Exceeded
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_avg = float("-inf")
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums) - k + 1):
            curr_avg = max(curr_avg, sum(nums[i:i+k])/k)
        return curr_avg
            
        
# Accepted solution
class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        curr_sum = 0
        max_sum = float('-inf')
        i = 0
        for j in range(len(nums)):
            if j < k:
                curr_sum += nums[j]
                max_sum = curr_sum
            else:
                curr_sum = curr_sum + nums[j] - nums[i]
                i += 1
                max_sum = max(max_sum, curr_sum)
        return max_sum / k
    
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums:
            return 0
        
        left = right = 0
        curr_sum = 0
        max_sum = float('-inf')
        while right < len(nums):
            while right - left != k or right < k:
                curr_sum += nums[right]
                right += 1

            max_sum = max(max_sum, curr_sum)
            curr_sum -= nums[left]
            left += 1
        return max_sum / k


      
# Refactored
def findMaxAverage(nums, k: int) -> float:
    curr_sum = 0
    for j in range(k):
        curr_sum += nums[j]
    res = curr_sum
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]
        res = max(res, curr_sum)
    return res / k
