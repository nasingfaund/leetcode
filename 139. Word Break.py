# memory limit - crap!
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def helper(curr_string):
            if curr_string == s:
                return True
            if len(curr_string) > len(s):
                return False
            for word in wordDict:
                if helper(curr_string + word):
                    return True
            return False
            
                
                
        return helper('')
        
# don't explore unneded branches:
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def helper(curr_string):
            if curr_string == '':
                return True
            for word in wordDict:
                if not curr_string.startswith(word):
                    continue
                if helper(curr_string.removeprefix(word)):
                    return True
            return False
                
        return helper(s)
        
