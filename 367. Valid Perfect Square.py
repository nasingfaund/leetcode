class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        first = 1
        second = num 
        
        while first<=second:
            middle = (first + second)//2
            if num == middle * middle:
                return True
            if num < middle*middle:
                second = middle - 1
            else:
                first = middle + 1
        return False
    
