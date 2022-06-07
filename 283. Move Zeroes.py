# TLE
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        left = len(nums) - 1
        while i < len(nums):
            if nums[i] == 0 and i < left:
                left -= 1
                j = i
                while j < len(nums) - 1:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    j += 1
            else:
                i += 1
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        return nums
