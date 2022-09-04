class Solution:
    def canPartition(self, alist):
        whole_sum = sum(alist)
        if whole_sum & 1:
            return False
        half_sum = whole_sum // 2

        @cache        
        def find(index, curr):

            if index >= len(alist) or curr > half_sum:
                return False
            if curr == half_sum:
                return True
            return find(index + 1, curr + alist[index]) or find(index + 1, curr)

        return find(0, 0)

        
class Solution:
    def canPartition(self, alist):
        whole_sum = sum(alist)
        if whole_sum & 1:
            return False
        half_sum = whole_sum // 2
        memo = {}

        def find(index, curr):
            if (index,curr) in memo:
                return memo[(index, curr)]

            if index >= len(alist) or curr > half_sum:
                return False
            if curr == half_sum:
                return True
            memo[(index, curr)] =  find(index + 1, curr + alist[index]) or find(index + 1, curr)

            return memo[(index, curr)]
        return find(0, 0)

    
    
    
class Solution:
    def canPartition(self, nums):
        total_sum = sum(nums)

        if total_sum & 2 == 1:
            return False

        half_sum = total_sum // 2
        aset = {0}

        for num in nums:
            subset = set()
            for elem in aset:
                if (elem + num) == half_sum:
                    return True
                subset.add(elem + num)
            aset |= subset
        return half_sum in aset
    
# two dimensional DP

# the last version
class Solution:
    def canPartition(self, alist):
        whole_sum = sum(alist)
        if whole_sum & 1:
            return False
        half_sum = whole_sum // 2
        dp = [[True] + [False]*half_sum for _ in range(len(alist))]
        
        for i in range(len(alist)):
            for num in range(1, half_sum + 1):
                if alist[i] <= half_sum:
                    dp[i][num] = dp[i-1][num] or dp[i-1][num - alist[i]]
                else:
                    dp[i][num] = dp[i-1][num]

        return dp[-1][-1]
    
class Solution:
    def canPartition(self, nums):
        total_sum = sum(nums)
        if total_sum & 1: return False
        
        half_sum = total_sum // 2
        
        dp = [[False]*len(range(half_sum + 1)) for _ in range(len(nums))]
        
        for i in range(len(dp)):
            dp[i][0] = True
            
        for i in range(len(nums)):
            for j in range(half_sum+1):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                    
        return dp[len(nums)-1][half_sum]
    
# Space optimized
class Solution:
    def canPartition(self, alist):
        whole_sum = sum(alist)
        if whole_sum & 1:
            return False
        half_sum = whole_sum // 2
        
        dp = [True] + [False]*half_sum
        
        for i in range(len(alist)):
            for num in range(half_sum, i, -1): # or range(half_sum, -1, -1)
                if alist[i] <= num:
                    dp[num] = dp[num] or dp[num - alist[i]]
        return dp[-1]
    
# DP with bitmasking 
class Solution:
    def canPartition(self, nums):
        whole_sum = sum(nums)
        if whole_sum & 1:
            return False
        half_sum = whole_sum // 2
        dp = 1
        for num in nums:
            dp |= dp << num
        return bool(dp & 1 << half_sum)

