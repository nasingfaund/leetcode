class Solution:
    def sortColors(self, nums: List[int]) -> None:
        first = 0
        second = len(nums) - 1
        i = 0
        while i <= second:
            if nums[i] == 0:
                nums[i], nums[first] = nums[first], nums[i]
                i+=1
                first += 1
            elif nums[i] == 1:
                i+=1
            else:
                nums[i], nums[second] = nums[second], nums[i]
                second -= 1
