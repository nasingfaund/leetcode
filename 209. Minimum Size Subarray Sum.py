# brute force 
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        first = 0
        second = 1
        smallest_length = float('inf')

        while first < second <= len(nums):
            if sum(nums[first:second]) >= target:
                smallest_length = min(smallest_length, second - first)
                first += 1
            else:
                second += 1
                
        if smallest_length == float('inf'):
            smallest_length = 0
                
        return smallest_length
      
      
# two pointers, complexity O(n)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        win_sum = 0
        first = 0
        
        for second in range(len(nums)):
            win_sum += nums[second]
            
            while win_sum >= target:
                min_len = min(min_len, second - first + 1)
                win_sum -= nums[first]
                first+=1
        if min_len == float('inf'):
            min_len = 0
        return min_len
                
        
