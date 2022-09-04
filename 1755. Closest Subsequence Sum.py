# tle
# time complexity: O(2^n)
# space complexity: O(2^n)
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        memo = {}
        nums.sort()
        def find(index, curr_sum):
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]
            if index == len(nums):
                return abs(curr_sum - goal)
            memo[(index, curr_sum)] = min(find(index + 1, curr_sum + nums[index]),  find(index +1, curr_sum))
            return memo[(index, curr_sum)]
        return find(0, 0)
      
      
      
# time complexity: O(2^(n/2))
# space complexity: O(2^(n/2))

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        length = len(nums)
        
        first = nums[:length//2]
        second = nums[length//2:]
        
        subsets_first, subsets_second = [], []
        
        def get_powerset(nums, index, curr, result):
            if index >= len(nums):
                result.append(curr)
                return 
            
            get_powerset(nums, index + 1, curr + nums[index], result)
            get_powerset(nums, index +1, curr, result)
            
        get_powerset(first, 0, 0, subsets_first)
        get_powerset(second, 0, 0, subsets_second)
        
        
        subsets_first_sum = sorted(subsets_first)
        subsets_second_sum = sorted(subsets_second)
        
        ans  = float('inf')
        for x in subsets_second_sum:
            diff = goal - x
            k = bisect_left(subsets_first_sum, diff)
            
            if k < len(subsets_first_sum): 
                ans = min(ans, subsets_first_sum[k] + x - goal)
            if 0 < k: 
                ans = min(ans, goal - x - subsets_first_sum[k-1])
        return ans 
            
# a bit improved version (faster)

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        length = len(nums)
        
        first = nums[:length//2]
        second = nums[length//2:]
        
        
        def get_powerset(nums):
            ans = {0}
            for x in nums: 
                ans |= {x + y for y in ans}
            return ans 
        
        
        subsets_first_sum = sorted(get_powerset(first))
        subsets_second_sum = sorted(get_powerset(second))
        
        ans  = float('inf')
        for x in subsets_second_sum:
            remain = goal - x
            k = bisect_left(subsets_first_sum, remain)
            
            if k<len(subsets_first_sum):
                ans=min(ans,abs(remain-subsets_first_sum[k]))
            if k>0:
                ans=min(ans,abs(remain-subsets_first_sum[k-1]))
        return ans 
            
