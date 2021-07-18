class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(1, len(prices)):
                if prices[j] <= prices[i] and j > i:
                    prices[i] = prices[i] - prices[j]
                    break
        return prices
