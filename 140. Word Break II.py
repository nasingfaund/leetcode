class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @cache
        def helper(string, curr):
            result = []
            if string == '':
                return [' '.join(curr)]
            for word in wordDict:
                if not string.startswith(word):
                    continue
                result += helper(string.removeprefix(word), curr + (word,))
            return result
        
        return helper(s, ())
        


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        @cache
        def helper(string, curr):
            if string == '':
                result.append(' '.join(curr))
                return 
            for word in wordDict:
                if not string.startswith(word):
                    continue
                sub_res = helper(string.removeprefix(word), curr + (word,))
        helper(s, ())
        return result
        
        
 
