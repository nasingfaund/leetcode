class Solution:
    def change(self, amount: int, coins) -> int:
        n = len(coins)
        
        dp = [[0]*(amount+1) for _ in range(n+1)]
        
        for j in range(len(dp)):
            dp[j][0] = 1
            
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if coins[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-coins[i-1]]
                        
        return dp[n][amount]
    
class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(1, amount + 1):
                if (j - coins[i]) >= 0:
                    dp[j] += dp[j - coins[i]]
        return dp[amount]

class Solution:
    def change(self, amount: int, coins) -> int:
        @lru_cache(maxsize=None)
        def dfs(amount, coins, idx, curr):
            if curr > amount or idx >= len(coins):
                return 0
            if amount == curr:
                return 1
            result = 0

            result += dfs(amount, coins, idx, curr + coins[idx])
            result += dfs(amount, coins, idx + 1, curr)
            return result

        return dfs(amount, tuple(coins), 0, 0)
