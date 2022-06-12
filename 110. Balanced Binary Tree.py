class Solution:
    def dfs(self, root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) != -1
