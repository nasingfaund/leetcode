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
class Solution:
    def firstBadVersion(self, n: int) -> int:
        def find(first, second):
            if first >= second:
                return first
            middle = (first + second) // 2
            
            if not isBadVersion(middle):
                if isBadVersion(middle + 1):
                    return middle  + 1
            else:
                if not isBadVersion(middle - 1):
                    return middle 
            
            if isBadVersion(middle):
                return find(first, middle - 1)
            else:
                return find(middle + 1, second)
        return find(1, n)
