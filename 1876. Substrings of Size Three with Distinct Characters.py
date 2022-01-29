# brute force, Complexity O(n^2)
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k = 3
        counter = 0
        for i in range(len(s)-k+1):
            if len(set(s[i:i+k])) == k:
                counter +=1
        return counter
      
# Complexity O(n)      
 class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        counter = 0
        k = 3
        for i in range(len(s) - k+1):
            if s[i] != s[i + 1] and s[i] != s[i + 2] and s[i + 1] != s[i + 2]:
                counter += 1
        return counter

# todo: Using siding window, generalized version
