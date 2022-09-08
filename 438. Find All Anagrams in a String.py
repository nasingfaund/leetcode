class Solution:
    def findAnagrams(self, s2: str, s1: str) -> List[int]:
        needle = Counter(s1)
        window_size = len(s1)

        freq_map = Counter()
        left = right = 0
        result = []
        while right < len(s2):
            if freq_map == needle:
                result.append(left)

            while right - left >= window_size:
                freq_map[s2[left]] -= 1
                if freq_map[s2[left]] == 0:
                    freq_map.pop(s2[left])
                left += 1

            freq_map[s2[right]] += 1
            right += 1
        if freq_map == needle:
            result.append(left)
        return result

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        result = []
        l1 = [0]*26 
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
            
        
        
# improved, removed duplication
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        result = []
        
        l1 = [0]*26
        l2 = [0]*26
        win_size = len(p)
        
        for i in range(win_size):
            l1[ord(p[i]) - ord('a')] +=1
            l2[ord(s[i]) - ord('a')] +=1
            
        if l1 == l2:
            result.append(0)
            
        for i in range(1, len(s) - win_size + 1):
            l2[ord(s[i + win_size -1]) - ord('a')] += 1
            l2[ord(s[i-1]) - ord('a')] -= 1
            
            if l1 == l2:
                result.append(i)
        
        return result
    
# Nice solution using Counter
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []

        dic_p = Counter(p)
        dic_s = Counter(s[:len(p)])

        if dic_s == dic_p:
            output.append(0)

        for i in range(1, len(s) - len(p) + 1):

            dic_p[s[i - 1]] += 1
            dic_p[s[i + len(p) - 1]] -= 1

            if dic_p[dic_p[s[i - 1]]] == 0:
                del dic_p[dic_p[s[i - 1]]]

            if dic_s == dic_p:
                output.append(i)

        return output
# Slight variation
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []

        dic_p = Counter(p)
        dic_s = Counter(s[:len(p) - 1])

        if dic_s == dic_p:
            output.append(0)

        for i in range(len(p) - 1, len(s)):
            dic_s[s[i]] += 1
            if dic_s == dic_p:
                output.append(i - len(p) + 1)
            dic_s[s[i - len(p) + 1]] -= 1
            if dic_s[s[i - len(p) + 1]] == 0:
                del dic_s[s[i - len(p) + 1]]

        return output
