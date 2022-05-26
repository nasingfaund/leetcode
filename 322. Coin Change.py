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
                    ans = min(find(coins, amount - coin) + 1, ans)
            return ans

        result = find(tuple(coins), amount)

        return result if result != float('inf') else -1
    
# BFS (we need to find shortest path)
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        queue = deque([[0, amount]])
        visited = {amount}

        while queue:
            curr, amount = queue.popleft()

            if amount == 0:
                return curr

            for coin in coins:
                value = amount - coin
                if value >= 0 and value not in visited:
                    queue.append([curr + 1, value])
                    visited.add(value)
        return -1

