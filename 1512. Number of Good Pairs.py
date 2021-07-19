class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashMap = {}
        res = 0
        for number in nums:            
            if number in hashMap:
                res += hashMap[number]
                hashMap[number] += 1
            else:
                hashMap[number] = 1
        return res
      
      
from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        for n in Counter(nums).values():
            counter += (n * (n - 1) // 2)
        return counter

        
