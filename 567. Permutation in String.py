
class Solution:
    def is_permutation(self, s1, s2):
        return sorted(s1) == s2
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        win_size = len(s1)
        s1 = sorted(s1) # firstly I was sorting s1 in is_permutation too for no reason, this one is passing
        for i in range(len(s2) - win_size+1):
            if self.is_permutation(s2[i:i+win_size], s1):
                return True
        return False
