# brute force TLE
class Solution:
    def canJump(self, nums) -> bool:
        # index = where to jump
        n = len(nums)
        @cache
        def find(index):
            if index >= n:
                return False
            if index == n - 1:
                return True

            for to_jump in range(index+1, index + nums[index]+1):  # 2, 2+1
                if find(to_jump):
                    return True
            return False

        return find(0)
      
# O(n), Space O(1)      
class Solution:
    def canJump(self, nums):
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True
