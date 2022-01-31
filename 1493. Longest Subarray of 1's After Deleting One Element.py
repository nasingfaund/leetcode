class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        start = 0
        max_ones_count = 0
        for end in range(len(nums)):
            if nums[end] == 1:
                max_ones_count +=1
            
            while end - start + 1 - max_ones_count > 1:
                if nums[start] == 1:
                    max_ones_count -=1
                start +=1
            
            max_len = max(max_len, end-start)

        return max_len

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        start = 0
        adict = {}
        for end in range(len(nums)):
            if nums[end] not in adict:
                adict[nums[end]] = 0
            adict[nums[end]] += 1

            while 0 in adict and adict[0] > 1:
                adict[nums[start]] -=1
                start +=1
                

            max_len = max(max_len, end-start)

        return max_len
