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
    
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = set()
        for i in range(len(nums)):
            index = abs(nums[i]) -1
            if nums[index] < 0:
                res.add(index+1)
            nums[index] = -nums[index]
        return res
    
    
    
class Solution(object):
    def findDuplicates(self, nums):
        ans = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        return nums
