# DP: Time complexity O(N^2)
class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        alist = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        dp = [0]*(max(alist, key=lambda x: x[1])[1]+1)
        for start_time, end_time, profit in alist:
            current_profit = dp[start_time] + profit
            if current_profit > dp[end_time]:
                for i in range(end_time, len(dp)):
                    dp[i] = max(dp[i], current_profit)
        return dp[-1]
        
        
# super inefficient solution, passes the half of tests, gives TLE (obviously). Bulshit code below
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        data = []
        for i in range(len(startTime)):
            data.append(((startTime[i], endTime[i]), profit[i]))

        data.sort(key=lambda pair: (pair[0][0], pair[0][1]))

        jobs = [obj[0] for obj in data]
        profit = [obj[1] for obj in data]

        self.ans = float('-inf')

        @cache
        def find(first, second, curr):
            for i in range(second + 1, len(jobs)):
                if jobs[i][0] >= jobs[second][1]:
                    find(first, i, curr + profit[i])
            self.ans = max(self.ans, curr)

        for i in range(len(jobs)):
            find(i, i, profit[i])
        return self.ans

    
