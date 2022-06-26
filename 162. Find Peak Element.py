class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums) - 1
    
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid + 1]:
                hi = mid
            else:
                lo = mid + 1
        return hi

    
class Solution:
    def binary_search(self, nums, lo, hi):
        if lo >= hi:
            return hi
        mid = (lo + hi) // 2
        if nums[mid] > nums[mid+1]:
            return self.binary_search(nums, lo, mid)
        else:
            return self.binary_search(nums, mid+1, hi)
            
    def findPeakElement(self, nums: List[int]) -> int:
        return self.binary_search(nums, 0, len(nums)-1)
