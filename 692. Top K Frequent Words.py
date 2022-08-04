
from collections import Counter
from itertools import chain
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        bucket = [[] for _ in range(len(words) + 1)]
        for key, count in c.items():
            bucket[count].append(key)
            bucket[count].sort()
        return list(chain(*bucket[::-1]))[:k]
        
        
