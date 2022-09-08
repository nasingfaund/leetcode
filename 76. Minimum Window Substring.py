class Solution:
    def minWindow(self, string: str, t: str) -> str:
        pattern = Counter(t)
        target = len(t)
        left = right = 0
        min_sub_str = ""
        while right < len(string):
            if pattern[string[right]] > 0:
                target -= 1
            pattern[string[right]] -= 1
            while target == 0:
                win_len = right - left + 1
                if not min_sub_str or win_len < len(min_sub_str):
                    min_sub_str = string[left: right + 1]
                pattern[string[left]] += 1
                if pattern[string[left]] > 0:
                    target += 1

                left += 1
            right += 1

        return min_sub_str
    
class Solution:
    def minWindow(self, s, t):
        need = collections.Counter(t)
        missing = len(t)
        start, end = 0, 0
        i, j = 0, 1
        while j < len(s)+1:  # enumerate(s, 1)
            char = s[j-1]
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1 
                missing += 1  
                if end == 0 or j - i < end - start:  
                    start, end = i, j
                i += 1  
            j+=1
        return s[start:end]
