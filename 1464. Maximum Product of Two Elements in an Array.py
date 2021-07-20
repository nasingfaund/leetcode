# brute force
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                m = max((nums[i]-1)*(nums[j]-1), m)
        return m
        
        
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = b = 0
        for n in nums:
            a, b = max(a, n), max(b, min(a, n))
        return (a-1) * (b-1)
      
      
import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        two_largest = heapq.nlargest(2, nums)
        return (two_largest[0]-1)*(two_largest[1]-1)
        
