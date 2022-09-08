class Solution:
    def characterReplacement(self, string: str, k: int) -> int:
        max_len = 0
        max_repeating = 0
        left = right = 0
        adict = defaultdict(int)
        while right < len(string):
            adict[string[right]] += 1

            max_repeating = max(max_repeating, adict[string[right]])

            if right - left + 1 - max_repeating > k:
                adict[string[left]] -= 1
                if adict[string[left]] == 0:
                    adict.pop(string[left])
                left += 1
            max_len = max(max_len, right - left + 1)
            right +=1
        return max_len

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_repeating = 0
        start = 0
        adict = {}
        for end in range(len(s)):
            if s[end] not in adict:
                adict[s[end]] = 0
            adict[s[end]] += 1

            max_repeating = max(max_repeating, adict[s[end]])

            if end - start + 1 - max_repeating > k:
                adict[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len
