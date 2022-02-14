class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[j] != nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        duplicateNumbers = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicateNumbers.append(nums[i])
        return duplicateNumbers
