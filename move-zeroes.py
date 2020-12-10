"""
https://leetcode.com/problems/move-zeroes/
"""

def move_zeroes(nums):
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1
    return nums

nums = [0, 1, 0, 3, 12]
print(move_zeroes(nums))
# [1, 3, 12, 0, 0]
