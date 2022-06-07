# time complexity: O(n), space complexity: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        adict = Counter()
        for num in nums:
            adict[num] += 1
        return adict.most_common()[0][0]
    
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
