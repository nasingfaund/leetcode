class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = set()
        def helper(curr, index):
            if len(curr) == len(nums):
                print(curr)
                result.append(curr[:])
                return
            for i in range(len(nums)):
                if i not in visited:
                    if i > 0 and i-1 not in visited and nums[i] == nums[i-1]:
                        continue
                    visited.add(i)
                    curr.append(nums[i])
                    helper(curr, i + 1)
                    curr.pop()
                    visited.remove(i)
        helper([], 0)
        return result 
      
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)
        def helper(curr,k, nums):
            if len(curr) ==k:
                result.append(curr[:])
                return
            for i in range(len(nums)):
                if i > 0  and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                helper(curr, k, nums[:i] + nums[i+1:])
                curr.pop()
        helper([],len(nums), nums)
        return result 
