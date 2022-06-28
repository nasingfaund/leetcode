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
    
# Time Complexity: O(n**2)        
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = [1]*len(pairs)
        
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
