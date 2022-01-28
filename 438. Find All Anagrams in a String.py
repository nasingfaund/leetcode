class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        result = []
        l1 = [0]*26 # todo: check correctness
        win_size = len(p)
        
        for i in range(len(p)):
            l1[ord(p[i]) - ord('a')] += 1
            
        l2 = [0]*26
        for i in range(win_size):
            l2[ord(s[i]) - ord('a')] +=1
            
        for i in range(len(s) - win_size + 1):
            if l1 == l2:
                result.append(i)
            if i + win_size == len(s):
                return result
            l2[ord(s[i + win_size]) - ord('a')] += 1
            l2[ord(s[i]) - ord('a')] -= 1

        
        return result
            
