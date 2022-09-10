class Solution:
    def longestPalindrome(self, s):
        unmatched_pairs = set() 
        pairs = 0
        for char in s:
            if char in unmatched_pairs:
                pairs += 1
                unmatched_pairs.remove(char)
            else:
                unmatched_pairs.add(char)
                
        return pairs * 2 + 1 if unmatched_pairs else pairs * 2
        
