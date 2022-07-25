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
        
# backtracking
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(left, right, stack):
            if left == right == n:
                result.append("".join(stack))
                return
            
            if left < n:
                stack.append('(')
                backtrack(left + 1, right, stack)
                stack.pop()
                
            if right < left:
                stack.append(')')
                backtrack(left, right + 1, stack)
                stack.pop()
        backtrack(0, 0, [])
        return res
   
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        left, right, ans = n, n, []
        
    
        def dfs(left, right, ans, string):
            if right < left:
                return

            if not left and not right:
                ans.append(string)

            if left:
                dfs(left -1, right, ans, string +"(")
            if right:
                dfs(left, right-1, ans, string + ")")
        
        dfs(left, right, ans, "")
        return ans
        
