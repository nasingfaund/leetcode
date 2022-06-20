from bisect import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)
        
# O(n)     
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
    
from bisect import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first = 0
        second = len(nums) - 1
        ans = len(nums)
        while first <= second:
            middle = first + (second - first)//2
            
            if target > nums[middle]:
                first = middle + 1
            else:
                second = middle - 1
                ans = middle
        return ans
                
