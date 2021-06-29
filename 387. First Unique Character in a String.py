from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        common = c.most_common()
        res = [k for k, i in common if i == 1]
        if res:
            return s.index(res[0])
        return -1
        
