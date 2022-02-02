# O(n//k) * O(k) * O(k^2 log k) = O((n*k^2logk) - check?

class Solution:
    def is_permutation(self, s1, s2):
        return sorted(s1) == s2 # O(k^2 log k), sorting O(k log k) and comparing O(k) 
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        win_size = len(s1)
        # s1 log s1
        s1 = sorted(s1) # firstly I was sorting s1 in is_permutation too for no reason, this one is passing
        for i in range(len(s2) - win_size+1): # O(n//k)
            window = s2[i:i+win_size] # O(k)
            if self.is_permutation(window, s1): # O(k^2 log k)
                return True
        return False

# runtime: O(n*k^2)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        d1 = Counter(s1)
        k = len(s1)
        for i in range(len(s2)):  # ---- O(n)
            sub = s2[i:i+k]  # ------ O(k)
            d2 = Counter(sub) # --- O(k)
            if d1 == d2:
                return True
        return False

    
# with array, Time Limit Exceeded
class Solution:
    def is_permutation(self, s1, s2):
        table = [0 for _ in range(26)]
        a_ord = ord('a')
        for i in range(len(s1)):
            table[ord(s1[i]) - a_ord] += 1
            
        for i in range(len(s2)):
            if table[ord(s2[i]) - a_ord] == 0:
                return False
            table[ord(s2[i]) - a_ord] -= 1
            if table[ord(s2[i]) - a_ord] < 0:
                return False
            
        return True
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        win_size = len(s1)
        s1 = sorted(s1)
        for i in range(len(s2) + win_size - 1):
            window = s2[i:i+win_size]
            self.is_permutation(window, s1)
        return False
    
    
# using array, passing
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_map = [0]*26
        a_ord = ord('a')
        for i in range(len(s1)):
            s1_map[ord(s1[i]) - a_ord] += 1
            
        for i in range(len(s2) - len(s1) + 1):
            s2_map = [0]*26
            for j in range(len(s1)):
                s2_map[ord(s2[i+j])-a_ord] +=1
            if s1_map == s2_map:
                return True

        return False
    
# Sliding Window
class Solution:
    def checkInclusion(self, s1, s2):
            if len(s1) > len(s2):
                return False
            l1 = [0]*26
            l2 = [0]*26
            for i in range(len(s1)):
                l1[ord(s1[i]) - ord('a')] += 1
                l2[ord(s2[i]) - ord('a')] += 1

            for i in range(len(s2)-len(s1)):
                if l1 == l2:
                    return True
                l2[ord(s2[i]) - ord('a')] -= 1
                l2[ord(s2[i + len(s1)]) - ord('a')] += 1
            return l1 ==l2 

    
# Optimized Sliding Window
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = [0] * 26
        s2_map = [0] * 26

        a_ord = ord('a')
        win_size = len(s1)
        for i in range(win_size):
            s1_map[ord(s1[i]) - a_ord] += 1
            s2_map[ord(s2[i]) - a_ord] += 1
            
        count = 0
        for i in range(26):
            if s1_map[i] == s2_map[i]:
                count +=1
                
        for i in range(len(s2) - len(s1)):
            r = ord(s2[i + win_size]) - a_ord
            l = ord(s2[i]) - a_ord
            
            if count == 26:
                return True
            s2_map[r] +=1
            if s2_map[r] == s1_map[r]:
                count+=1
            elif s2_map[r] == s1_map[r] + 1:
                count -=1
            s2_map[l] -=1
            if s2_map[l] == s1_map[l]:
                count +=1
            elif s2_map[l] == s1_map[l] - 1:
                count -=1
        return count == 26
    
# frequency map/educative
class Solution:
    def checkInclusion(self, pattern, string):
        start = 0
        matched = 0
        char_frequency = {}

        for i in range(len(pattern)):
            if pattern[i] not in char_frequency:
                char_frequency[pattern[i]] = 0
            char_frequency[pattern[i]] += 1

        for end in range(len(string)):
            if string[end] in char_frequency:
                char_frequency[string[end]] -= 1
                if char_frequency[string[end]] == 0:
                    matched += 1

            if matched == len(char_frequency):
                return True

            if end >= len(pattern) - 1:
                left_char = string[start]
                start += 1
                if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                        matched -= 1
                    char_frequency[left_char] += 1

        return False
        
