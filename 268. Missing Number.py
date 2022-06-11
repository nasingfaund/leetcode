class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        full_sum = (n+1)*n//2
        return full_sum - sum(nums)
       
 class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            result ^= i
            result ^= nums[i]
        return result
        

# elegant Python solution https://leetcode.com/problems/missing-number/discuss/69832/1%2B-lines-Ruby-Python-Java-C%2B%2B
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums + range(len(nums)+1))
        

# todo: why this works?
def missingNumber(self, nums):
    n = len(nums)
    return reduce(operator.xor, nums) ^ [n, 1, n+1, 0][n % 4]
    
# Sum, without formula.
def missingNumber(self, nums):
    miss = i = 0
    for num in nums:
        miss += (i+1)- num
        i+=1
    return miss

# Set/array difference
def missingNumber(self, nums):
    return (set(range(len(nums)+1)) - set(nums)).pop()
