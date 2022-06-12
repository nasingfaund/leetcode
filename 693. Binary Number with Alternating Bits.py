class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = None
        while n:
            rem = n % 2 
            if prev is not None and prev == rem:
                return False
            prev = rem
            n = n//2
        return True
            
class Solution:
  def hasAlternatingBits(self, n: int) -> bool:
      #      10101010101
      #  +    1010101010    ( number >> 1 )
      #  ---------------
      #  =   11111111111
      #  &  100000000000
      #  ---------------
      #  =             0    ( power of two )
      tmp  = (n >> 1) + n 
      return (tmp & tmp + 1) == 0
            
        
