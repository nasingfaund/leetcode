class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        ans = 0
        pref_sum = 0
        d = {0: 1}

        for num in nums:
            pref_sum = pref_sum + num
            diff = pref_sum - k

            if diff in d:
                ans += d[diff]

            if pref_sum not in d:
                d[pref_sum] = 1
            else:
                d[pref_sum] += 1
        return ans
