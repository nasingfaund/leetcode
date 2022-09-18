class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        
        longest_sequence = 1
        longest_curr = 1
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i] + 1 == nums[i+1]:
                longest_curr += 1
            else:
                longest_sequence = max(longest_curr, longest_sequence)  
                longest_curr = 1
        return max(longest_sequence, longest_curr)
                
        
