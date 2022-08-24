class Solution:
    def reverse(self, x: int) -> int:
        is_negative = True if x < 0 else False
        if is_negative:
            x*=-1
        result = 0
        while x:
            rem = x % 10
            x= x//10
            result = result*10 + rem
        if result >= 2**31 - 1 or result <= -2*31:
            return 0
            
        return -result if is_negative else result
        
