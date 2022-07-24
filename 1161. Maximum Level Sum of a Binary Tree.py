class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        result = defaultdict(int)
        
        def dfs(root, level):
            
            if not root:
                return
            result[level+1] += root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        dfs(root, 0)
        return max(result, key=result.get)
