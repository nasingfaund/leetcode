class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        minSoFar = prices[0]
        for i in range(1, n):
            ans = max(ans, prices[i] - minSoFar)
            minSoFar = min(minSoFar, prices[i])
        return ans
