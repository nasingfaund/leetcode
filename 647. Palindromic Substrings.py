class Solution:
    def countSubstrings(self, s):
        count = 0
        for j in range(len(s) + 1):
            for i in range(j):
                if s[i:j] == s[i:j][::-1]:
                    count += 1
        return count
