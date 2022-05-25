class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [amount + 1] *(amount + 1)
        dp[0] = 0
        
        for i in range(1, len(dp)):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] <= amount else -1     
        
        
