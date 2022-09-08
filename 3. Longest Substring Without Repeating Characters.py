class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        left = right = 0
        adict = defaultdict(int)
        max_len = 0
        while right < len(string):
            adict[string[right]] += 1

            while adict[string[right]] > 1:
                adict[string[left]] -= 1
                if adict[string[left]] == 0:
                    adict.pop(string[left])
                left += 1

            max_len = max(max_len, right - left + 1)

            right += 1

        return max_len

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
    
class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        
        start = 0
        max_length = 0
        adict = {}

        for end in range(len(s)):
            if s[end] in adict:
                start = max(start, adict[s[end]] + 1)
            adict[s[end]] = end
            max_length = max(max_length, end - start + 1)
        return max_length
