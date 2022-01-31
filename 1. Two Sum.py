# https://leetcode.com/problems/two-sum/
    
    
# Brute force 
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Two-pass Hash Table
def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, v in enumerate(nums):
        seen[v] = i

    for i, v in enumerate(nums):
        rem = target - v

        if rem in seen and seen[rem] != i:
            return [seen[rem], i]

# One-pass Hash Table
def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, v in enumerate(nums):
        rem = target - v

        if rem in seen:
            return [seen[rem], i]

        seen[v] = i
