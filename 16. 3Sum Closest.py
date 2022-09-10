# Time complexity O(n^2), Space complexity O(1)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close_sum = float('inf')
        prev = float('inf')
        first = 0
        while first < len(nums):
            second = first + 1
            third = len(nums) - 1
            while second < third:
                sum3 = nums[first] + nums[second] + nums[third]
                if sum3 == nums:
                    return sum3
                if abs(target - sum3) < prev: 
                    close_sum = sum3
                    prev = abs(target - sum3)

                if sum3 < target:
                    second +=1
                else:
                    third -=1
            first += 1

        return close_sum

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr = nums[left] + nums[right] + nums[i]
                if curr >= target:
                    right -= 1
                else:
                    left += 1
                if abs(curr - target) < abs(res - target):
                    res = curr
        return res
