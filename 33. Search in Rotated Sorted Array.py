class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the minimum element
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
                
        start = lo
        lo = 0
        hi = len(nums) - 1
        
        # find from which side to search 
        if target >= nums[start] and target <= nums[hi]:
            lo = start 
        else:
            hi = start
            
        # run general binary search
        while lo <= hi:
            middle = (lo + hi) // 2
            if nums[middle] == target:
                return middle
            
            if nums[middle] > target:
                hi = middle - 1 
            else:
                lo = middle + 1
        return -1
            
        
