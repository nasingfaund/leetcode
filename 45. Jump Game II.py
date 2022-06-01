# O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest = 0
        left = right = 0
        while right < len(nums) - 1:
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            jumps += 1

        return jumps

class Solution:
    def jump(self, nums: List[int]) -> int:
        @cache
        def find(index, steps):
            if index >= len(nums):
                return float('inf')
            if index == len(nums) - 1:
                # print(steps)
                return steps

            ans = float('inf')
            for i in range(index + 1, nums[index] + index + 1):
                ans = min(ans, find(i, steps + 1))

            return ans

        return find(0, 0)
# time complexity O(N!), Space Complexity O(N)
class Solution:
    def jump(self, nums, pos=0):
        if pos >= len(nums) - 1:
            return 0
        minJumps = float('inf')
        for i in range(1, nums[pos] + 1):
            minJumps = min(minJumps, 1 + self.jump(nums, pos + i))
        return minJumps
# TLE
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: float('inf'))
        def find(index):
            if index >= len(nums)-1:
                return 0
            if dp[index] != float('inf'):
                return dp[index]

            for i in range(1, nums[index] + 1):
                dp[index] = min(dp[index], find(i+index)+1)
            
            return dp[index]

        return find(0)
