from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        res = ''
        for char, count in sorted(c.items(), key=lambda x: x[1], reverse=True):
            res += char*count
        return res
        
        
# One-liner
from collections import Counter
from operator import itemgetter
class Solution:
    def frequencySort(self, s: str) -> str:
        # "".join(char * times for char, times in collections.Counter(s).most_common())
        return ''.join(char*count for char, count in sorted(Counter(s).items(), key=itemgetter(1), reverse=True))
        
        
 # bucket sorting
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        bucket = [[] for _ in range(len(s)+1)]
        
        for key, count in c.items():
            bucket[count].append(key)
        
        return ''.join(i*c[i] for i in list(chain(*bucket))[::-1])
    
from queue import PriorityQueue
class Solution:
    def frequencySort(self, s: str) -> str:
        pq = PriorityQueue()

        c = Counter(s)

        for key, count in c.items():
            pq.put((-count, key))

        res = ''

        while not pq.empty():
            count, char = pq.get()
            res += -count * char
        return res
