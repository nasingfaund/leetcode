class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        first = 0
        last = len(nums) -1
        while first < last:
            middle = (first + last) // 2
            if nums[middle] == target:
                return True
            
            if nums[middle] > nums[last]:
                if nums[first] <= target < nums[middle]:
                    last = middle - 1
                else:
                    first = middle + 1
            elif nums[middle] < nums[last]:
                if nums[middle] < target <= nums[last]:
                    first = middle + 1
                else:
                    last = middle - 1
            else:
                last -= 1
            
        return nums[first] == target
