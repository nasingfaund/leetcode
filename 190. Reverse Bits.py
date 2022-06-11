class Solution:
    def reverseBits(self, n: int) -> int:
        if n==0:
            return 0
        value = 0
        for i in range(32):
            value <<= 1
            if n & 1 == 1:
                value +=1
            n>>=1
        return value
        
