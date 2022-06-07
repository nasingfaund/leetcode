class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        adict = Counter()
        for num in nums:
            adict[num] += 1
        return adict.most_common()[0][0]
