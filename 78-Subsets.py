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
