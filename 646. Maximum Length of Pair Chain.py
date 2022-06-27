class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda pair: pair[1])
        curr = 1
        last = pairs[0][1]
        for i in range(1, len(pairs)):
            if pairs[i][0] > last:
                curr += 1
                last = pairs[i][1]
                
        return curr
        
