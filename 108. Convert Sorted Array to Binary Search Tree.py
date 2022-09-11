class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_bst(nums, start, end):
            if end < start:
                return 
            
            mid = (start + end) // 2
            
            n  = TreeNode(nums[mid])
            n.left = build_bst(nums, start, mid -1)
            n.right = build_bst(nums, mid+1, end)
            
            return n
        return build_bst(nums, 0, len(nums)-1)
            
        
