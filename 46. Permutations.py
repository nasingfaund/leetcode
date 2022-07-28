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
    
class Solution(object):
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            others = nums[:i] + nums[i+1:]
            other_permutations = self.permute(others)
            for permutation in other_permutations:
                result.append([nums[i]] + permutation)
        return result
    
def backtracking(res, visited, subset, nums):
    if len(subset) == len(nums):
        res.append(subset)
    for i in range(len(nums)):
        if i not in visited:
            visited.add(i)
            backtracking(res, visited, subset + [nums[i]], nums)
            visited.remove(i)
            
class Solution(object):
    def permute(self, nums):
        result = []
        def _permute(nums, curr):
            if not nums:
                result.append(list(curr))
                return 
            for i in range(len(nums)):
                curr.append(nums[i])
                _permute(nums[:i] + nums[i+1:], curr)
                curr.pop()
        _permute(nums, [])
        return result
                
    
def find_permutations(nums):
    result = []
    permutations = deque([[]])
    for num in nums:
        for _ in range(len(permutations)):
            old_permutation = permutations.popleft()

            for j in range(len(old_permutation) + 1):
                new_permutation = list(old_permutation)
                new_permutation.insert(j, num)
                if len(new_permutation) == len(nums):
                    result.append(new_permutation)
                else:
                    permutations.append(new_permutation)

    return result

def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def _permute(perm, nums):
            if len(nums) == 0:
                result.append(list(perm))
            else:
                for i in range(len(nums)):
                    perm.append(nums.pop(0))
                    _permute(perm, nums)
                    nums.append(perm.pop())
        _permute([], list(nums))
        return result

