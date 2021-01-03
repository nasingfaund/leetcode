class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y
        res = 0
        while n != 0:
            res += (1 & n)
            n >>=1
        return res
        
# one liner - bin(x^y).count('1')
