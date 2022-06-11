class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for i in range(len(s)):
            if s[i] in mapping:
                stack.append(s[i])
            else: # no need to check if s[i] in mapping.values()
                if not stack:
                    return False
                elem = stack.pop()
                if s[i] != mapping[elem]:
                    return False
        if stack: 
            return False
        
        return True
