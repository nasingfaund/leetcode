# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def moveZeroes(self, nums: list) -> None:
        left = right = 0
        while right < len(nums):
            if nums[right] != 0 and nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]

            if nums[left] != 0:
                left += 1
                
            right += 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        return nums
