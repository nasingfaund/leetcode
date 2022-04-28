class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        nums.sort()
        for num in nums:
            for i in range(len(subsets)):
                subset = list(subsets[i])
                subset.append(num)
                if subset not in subsets:
                    subsets.append(subset)
        return subsets
