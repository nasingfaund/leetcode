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
        
        
        
