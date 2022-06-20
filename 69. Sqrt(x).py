class Solution:
    def mySqrt(self, x: int) -> int:
        first = 0
        last = x
        while first <= last:
            mid = first + (last- first) // 2
            
            if mid*mid<=x < (mid + 1) * (mid + 1):
                return mid
            
            if x < mid*mid:
                last = mid - 1
            else:
                first = mid + 1
