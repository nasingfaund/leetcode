class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k % len(nums)):
            elem = nums.pop()
            nums.insert(0, elem)
        
        
# reverse the first n - k elements
# reverse the rest of them
# reverse the entire array        
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        end = len(nums) - 1
        k = k % len(nums)
        self.reverse(nums, 0, end - k)
        self.reverse(nums, end - k + 1, end)
        self.reverse(nums, 0, end)
        return nums
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
