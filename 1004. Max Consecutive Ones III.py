class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        max_len = 0
        adict = defaultdict(int)
        max_repeating = 0
        while right < len(nums):
            adict[nums[right]] += 1
            if nums[right] == 1:
                max_repeating = max(max_repeating, adict[nums[right]])
            
            while right -  left + 1 - max_repeating > k:
                adict[nums[left]] -= 1
                if adict[nums[left]] == 0:
                    adict.pop(nums[left])
                left += 1
            max_len = max(max_len, right - left + 1)
            right +=1
        return max_len
                
            
            
        
