class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res= 0
        for i in nums:
            res ^=i
        return res
        
        
        
        
#one liner
singleNumber2 = labda nums: reduce(lambda x, y: x ^ y, nums)
