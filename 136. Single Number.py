"""
Other solutions - https://leetcode.com/problems/single-number/discuss/43000/Python-different-solutions.
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums)
        
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res= 0
        for i in nums:
            res ^=i
        return res
        
        
#one liner
singleNumber2 = labda nums: reduce(lambda x, y: x ^ y, nums)
