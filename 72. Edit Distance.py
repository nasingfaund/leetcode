# levinstein distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def helper(i, j):
            if i  == j == 0:
                return 0
            if j == 0:
                return i
            if i == 0:
                return j
            if word1[i-1] == word2[j-1]:
                return helper(i-1, j-1)
            return min(
                helper(i, j-1),
                helper(i-1, j),
                helper(i-1, j-1)
            )+1
        return helper(len(word1), len(word2))
        
