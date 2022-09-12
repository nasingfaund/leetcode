class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: # edge case! Important!
            return 0
        product = 1
        first = second = 0
        count = 0
        while second < len(nums):
            product *= nums[second]
                
            while product >= k and first < len(nums):
                product /= nums[first]
                first += 1
                
            count += second - first + 1
            second += 1
                

        return count
