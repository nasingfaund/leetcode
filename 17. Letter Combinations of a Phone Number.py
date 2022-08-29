# pythonic
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return map(''.join, product(*map(mapping.get, digits)))

       
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        if not digits:
            return []

        result = ['']
        for char in digits:
            letters = digit_map.get(char, '')
            result = [prefix+letter for prefix in result for letter in letters]
            
        return result    
    
    
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(digits, curr, index):
            if len(digits) == index:
                result.append(''.join(curr))
                return 
            
            for i in mapping[digits[index]]:
                curr.append(i)
                backtrack(digits, curr, index + 1)
                curr.pop()
        if not digits:
            return []
        result = []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        backtrack(digits, [], 0)
        return result
