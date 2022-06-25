class Solution:
    def arrangeCoins(self, n: int) -> int:
        first = 0
        second = n
        while first <= second:
            middle = (first + second) // 2
            curr = middle * (middle + 1) // 2
            if curr == n:
                return middle
            if n < curr:
                second = middle -1
            else:
                first = middle + 1
        return second
        
        
