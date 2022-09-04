class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = set()
        for i in range(len(nums)-1):
            curr_sum = nums[i] + nums[i+1]
            if curr_sum in sums:
                return True
            sums.add(curr_sum)
        return False
