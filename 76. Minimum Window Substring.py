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
