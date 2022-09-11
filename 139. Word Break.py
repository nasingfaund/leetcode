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
        
