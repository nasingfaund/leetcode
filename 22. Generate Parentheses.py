class Solution:
    def is_valid(self, curr):
        stack = []
        for char in curr:
            if char == '(':
                stack.append(char)
            else:
                if not stack:
                    return False
                val = stack.pop()
                if val != '(':
                    return False
        return not stack

    def generateParenthesis(self, n):
        result = []

        def _gen(n, index, curr):
            if len(curr) == 2 * n:
                if self.is_valid(curr):
                    result.append(curr)
                return
            _gen(n, index + 1, curr + '(')
            _gen(n, index + 1, curr + ')')

        _gen(n, 0, "")
        return result
    
class Solution:
    def generateParenthesis(self, n):
        result = []
        def generate(curr, left, right, n):
            if len(curr) == 2 * n:
                result.append(curr)
            if left < n:
                generate(curr + '(', left + 1, right, n)
            if right < left:
                generate(curr + ')', left, right + 1, n)
        
        generate('', 0, 0, n)
        return result     
        

        
        
