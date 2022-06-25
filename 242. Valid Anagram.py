class Solution:
    def count_chars(self,string):
        adict = defaultdict(int)
        for char in string:
            adict[char] += 1
        return adict
    def isAnagram(self, s: str, t: str) -> bool:
        return self.count_chars(s) == self.count_chars(t)
        
