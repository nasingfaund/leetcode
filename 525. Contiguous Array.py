class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = 0
        adict = {0: -1}
        ans = 0
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                prefix_sum -= 1
            elif num == 1:
                prefix_sum += 1
            if prefix_sum in adict:
                ans = max(ans, i - adict[prefix_sum])
            else:
                adict[prefix_sum] = i
        return ans
