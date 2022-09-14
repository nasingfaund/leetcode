# bellmand ford algorithm

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        result = defaultdict(lambda: float('inf'))
        result[src] = 0
        
        for _ in range(k+1):
            temp = result.copy()
            for source, destination, weight in flights:
                temp[destination] = min(temp[destination], result[source] + weight)
            result = temp                
        return result[dst] if result[dst] != float('inf') else -1
        
        
