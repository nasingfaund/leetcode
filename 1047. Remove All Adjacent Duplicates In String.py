# time limit memory 
class Solution:
    def removeDuplicates(self, s: str) -> str:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                return self.removeDuplicates(s[:i] + s[i+2:])
        return s
                
        
# accepted with stack        
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
                
# two pointers
def removeDuplicates(s: str) -> str:
    i = 0
    s = list(s)
    for j in range(len(s)):
        s[i] = s[j]
        if i > 0 and s[i - 1] == s[i]:
            i -= 2
        i += 1
    return ''.join(s[:i])

