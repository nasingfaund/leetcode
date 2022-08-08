class Solution:
    def find_dist(self, x, y):
        return math.sqrt(x**2 + y**2)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        adict =  []
        
        for x, y in points:
            dist = self.find_dist(x, y)
            adict.append([(x, y), dist])
        adict.sort(key= lambda x: x[1])
        return [p for p, v in adict[:k]]
        
        
class Solution:
    def get_distance(self, x, y):
        return x*x + y*y
    
    def kClosest(self, P, k):
        heap = []
        for i, (x, y) in enumerate(P):
            d = self.get_distance(x, y)
            if len(heap) == k:
                heappushpop(heap, (-d, i))     
            else: 
                heappush(heap, (-d, i))
        return [P[i] for (_, i) in heap]
