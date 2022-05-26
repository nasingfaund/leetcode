# Time complexity: O(amount*len(coins)), Space Complexity O(amount)
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [amount + 1]*(amount+1)
        dp[0] = 0
        
        for i in range(1, len(dp)):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i-coin]+1, dp[i])
        return dp[-1] if dp[-1] <= amount else -1

    
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        memo = {}

        def find(coins, amount: int) -> int:
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            memo[amount] = float('inf')

            for coin in coins:
                if coin <= amount:
                    memo[amount] = min(find(coins, amount - coin) + 1, memo[amount])

            return memo[amount]

        result = find(coins, amount)

        return result if result != float('inf') else -1
    
    
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        @cache
        def find(coins, amount: int) -> int:
            if amount == 0:
                return 0

            ans = float('inf')
            for coin in coins:
                if coin <= amount:
                    sub_ans = find(coins, amount - coin)
                    ans = min(sub_ans + 1, ans)
            return ans

        result = find(tuple(coins), amount)

        return result if result != float('inf') else -1
