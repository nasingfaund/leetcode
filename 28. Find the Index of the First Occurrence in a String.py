# dirty version: O(n^2)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)):
            pointer = 0
            start = i
            while pointer < len(needle) and i< len(haystack) and haystack[i] == needle[pointer]:
                pointer += 1
                i+= 1
            if pointer == len(needle):
                return start
        return -1
        
