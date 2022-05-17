class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path +[nums[i]], res)


class Solution:
    def permute(self, nums):
        stack = [(nums, [])]
        res = []
        while stack:
            nums, path = stack.pop()
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                stack.append((nums[:i] + nums[i+1:], path+[nums[i]]))
        return res
