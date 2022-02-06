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

# improved, not mine
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        first = 0
        while first < len(nums) - 2:
            second = first + 1
            third = len(nums) - 1
            while second < third:
                sum3 = nums[first] + nums[second] + nums[third]
                if sum3 == target:
                    return sum3
                
                if abs(sum3 - target) < abs(result - target):
                    result = sum3
                
                if sum3 < target:
                    second += 1
                elif sum3 > target:
                    third -= 1
            first += 1
            
        return result
