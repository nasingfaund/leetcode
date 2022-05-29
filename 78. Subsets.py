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
        for i in range(1 << len(nums)):
            aset = []
            for j in range(len(nums)):
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
