class Solution:
    result = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left) 
            right = dfs(root.right)
            print(left, right)
            
            curr = max(root.val, left+root.val, right+root.val, left + right + root.val)
            self.result = max(self.result, curr)
            return max(root.val, left+root.val, right+root.val)
        dfs(root)
        return self.result
