class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        first = 0
        last = len(nums) - 1
        while first <= last:
            if abs(nums[first]) >= abs(nums[last]):
                result.insert(0, nums[first]**2)
                first +=1
            else:
                result.insert(0, nums[last]**2)
                last -=1
        return result
        
