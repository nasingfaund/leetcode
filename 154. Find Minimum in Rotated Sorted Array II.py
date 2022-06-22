class Solution:
    def findMin(self, nums: List[int]) -> int:
        first = 0
        second = len(nums) - 1
        while first < second:
            middle = first + (second - first) // 2
            if nums[first] <= nums[second]:
                second -= 1
            elif nums[middle] > nums[second]:
                first = middle + 1
            else:
                second = middle
        return nums[first]
        
