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
        left = right = 0
        curr_sum = 0
        min_length = float('inf')
        while right < len(nums):
            curr_sum += nums[right]

            while curr_sum >= target:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            right += 1

        if min_length == float('inf'):
            min_length = 0

        return min_length

        
