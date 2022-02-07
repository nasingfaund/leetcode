class Solution:
    def backspaceCompare(self, S, T):
        l1 = self.stack(S)
        l2 = self.stack(T)
        return l1 == l2
        
    
    def stack(self, string):
        stack = []
        for char in string:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return stack
