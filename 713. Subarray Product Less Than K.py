class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        product = 1
        count = 0
        first = 0
        for second in range(len(nums)):
            product *= nums[second]
            while product >= k:
                product /= nums[first]
                first +=1
            count += second - first + 1
        return count
