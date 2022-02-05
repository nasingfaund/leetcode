# time coplexity O(n), space complexity O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        first = 0
        for i in range(1, len(nums)):
            if nums[first] != nums[i]:
                nums[first + 1] = nums[i]
                first +=1
        return first + 1
