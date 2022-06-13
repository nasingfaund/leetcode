class Solution:
    def pathSum(self, root, targetSum):
        paths = []
        if not root:
            return paths
        def dfs(root, curr_sum, path):
            if not root:
                return
            if curr_sum == targetSum and not root.left and not root.right:
                paths.append(path)
            if root.left:
                dfs(root.left, curr_sum + root.left.val, path + [root.left.val])
            if root.right:
                dfs(root.right, curr_sum + root.right.val, path + [root.right.val])

        dfs(root, root.val, [root.val])
        return paths

class Solution:
    def _pathSum(self, root, targetSum, curr, paths):
        if not root:
            return  paths
        
        curr.append(root.val)
        
        if root.val == targetSum and not root.left and not root.right:
            paths.append(list(curr))
        else:
            self._pathSum(root.left, targetSum-root.val, curr, paths)
            self._pathSum(root.right, targetSum-root.val, curr, paths)
        del curr[-1]
        
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        self._pathSum(root, targetSum, [], paths)
        return paths
        
        
        
