# std solution
class Solution:
    def subsets(self, nums: List[int], index=0) -> List[List[int]]:
        result = []
        for i in range(len(nums)+1):
            result += itertools.combinations(nums, i)
        return result
    
class Solution:
    def subsets(self, nums: List[int], index=0) -> List[List[int]]:
        for i in range(len(nums)+1):
            for subset in itertools.combinations(nums, i):
                yield subset

# Time Complexity: O(n*2^n), Space Complexity: O(n*2^n)
# bit manipulation
class Solution:
    def subsets(self, nums):
        res = []
        for i in range(1 << len(nums)):
            v = bin(i)[2:]
            aset = []
            if len(v) != len(nums):
                v = v.zfill(len(v) + (len(nums) - len(v)))

            for j, value in enumerate(v):
                if value == '1':
                    aset.append(nums[j])
            if aset not in res:
                res.append(aset)
        return res


class Solution:
    def subsets(self, nums):
        res = []
        n = len(nums)
        for i in range(1 << n):
            aset = []
            for j in range(n):
                value = (1 << j) & i #  value = (i >> j) & 1
                if value:
                    aset.append(nums[j])
            res.append(aset)
        return res

        
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in range(len(nums)):
            for j in range(len(result)):
                subset = list(result[j])
                subset.append(nums[i])
                result.append(subset)
        return result
    
# backtracking 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(nums, index, path, result):
            result.append(path)
            for i in range(index, len(nums)):
                dfs(nums, i+1, path + [nums[i]], result)
        dfs(nums, 0, [], result)
        return result
    

# backtracking
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(index, curr, k):
            if len(curr) == k:
                result.append(list(curr))
                return 
            for i in range(index, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr, k)
                curr.pop()

        for k in range(len(nums) + 1):
            backtrack(0, [], k)
        return result
    
def subsets(nums: List[int]) -> List[List[int]]:
    subsets = []
    expected_subsets = 2 ** len(nums)

    def generate_subset(subset, nums):
        if len(subsets) >= expected_subsets:
            return
        if len(subsets) < expected_subsets:
            subsets.append(subset)
        for i in range(len(nums)):
            generate_subset(subset + [nums[i]], nums[i + 1:])

    generate_subset([], nums)
    return subsets


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result= []
        def powerset(alist, index, curr):
            if index == len(alist):
                result.append(curr)
                return 

            powerset(alist, index + 1, curr + [alist[index]]) 
            powerset(alist, index + 1, curr)
        
        powerset(nums, 0, [])
        return result
    
# I love generators
class Solution:
    def subsets(self, nums: List[int], index=0) -> List[List[int]]:
        def powerset(alist, index, curr):
            if index == len(alist):
                yield curr
                return 

            yield from powerset(alist, index + 1, curr + [alist[index]])  
            yield from powerset(alist, index + 1, curr)
        
        yield from powerset(nums, 0, [])
