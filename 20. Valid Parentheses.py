class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        stack = []
        for i in range(len(s)):
            if s[i] in mapping.keys():
                stack.append(s[i])

            if s[i] in mapping.values():
                if not stack:
                    return False
                val = stack.pop()
                if mapping[val] != s[i]:
                    return False
        if stack:
            return False
        return True
