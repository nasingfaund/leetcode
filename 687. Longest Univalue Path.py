class Solution:
    result = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            left_val = right_val = 0
            if root.left and root.left.val == root.val:
                left_val = left + 1
            if root.right and root.right.val == root.val:
                right_val = right + 1
                
            self.result = max(self.result, left_val + right_val)
            
            return max(left_val, right_val)
            
        dfs(root)
        return self.result
