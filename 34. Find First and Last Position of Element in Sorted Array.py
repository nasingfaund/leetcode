class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx1 = self.lower_bound(nums, target)
        idx2 = self.lower_bound(nums, target + 1) -1
        if idx1 < len(nums) and nums[idx1] == target:
            return [idx1, idx2]
        else:
            return [-1, -1]

    def lower_bound(self, nums, target):
        first = 0
        last = len(nums) - 1

        while first <= last:
            mid = (first + last) // 2
            pivot = nums[mid]

            if target > pivot:
                first = mid + 1
            else:
                last = mid - 1
        return first
