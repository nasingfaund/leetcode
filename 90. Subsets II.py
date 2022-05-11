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

    
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        start_index, end_index = 0, 0
        for i in range(len(nums)):
            start_index = 0
            if i >= 1 and nums[i] == nums[i-1]:
                start_index = end_index
                
            end_index = len(result)
            for j in range(start_index, end_index):
                sub = list(result[j])
                sub.append(nums[i])
                result.append(sub)
        return result
                
            
