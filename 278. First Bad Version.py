class Solution:
    def firstBadVersion(self, n: int) -> int:
        first = 1
        last = n
        
        while first <= last:
            middle = (first + last) // 2

            if isBadVersion(middle):
                last = middle - 1
                if not isBadVersion(last):
                    return middle
            else:
                first = middle + 1
                if isBadVersion(first):
                    return first
