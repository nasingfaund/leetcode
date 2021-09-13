class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        seen = {}
        longest = 0
        r = l = 0
        while r < len(s):
            if s[r] in seen:
                l = max(l, seen[s[r]] + 1)
            longest = max(longest, r - l + 1)
            seen[s[r]] = r
            r += 1

        return longest
