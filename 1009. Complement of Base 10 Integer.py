class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1 
        num = int((math.log(n) / 
                math.log(2)) + 1);
        for i in range(num):
            mask = 1 << i
            n = mask ^ n
        return n        
            
        
class Solution:
      def bitwiseComplement(self, N: int) -> int:
            c = 1
            while c < N: 
                c = (c << 1) + 1
            return N ^ c
