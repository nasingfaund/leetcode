class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums  = nums2
        ans = [0 for _ in nums]
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            ans[i] = stack[-1] if stack else -1
            stack.append(nums[i])
        return [ans[nums2.index(i)] for i in nums1]


