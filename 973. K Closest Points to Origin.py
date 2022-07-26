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
        
        
