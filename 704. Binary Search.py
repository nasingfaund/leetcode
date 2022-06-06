class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def _search(nums: List[int], target: int, low, high) -> int:
            middle = (low + high) // 2
            if high < low:
                return -1

            if nums[middle] == target:
                return middle

            if target > nums[middle]:
                return _search(nums, target, middle + 1, high)
            elif target < nums[middle]:
                return _search(nums[:middle], target, low, middle-1)

        return _search(nums, target, 0, len(nums) - 1)
    
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            print(middle)
            
            if target == nums[middle]:
                return middle
            
            if target > nums[middle]:
                left = middle + 1
            else:
                right= middle - 1
                
        return -1
            
