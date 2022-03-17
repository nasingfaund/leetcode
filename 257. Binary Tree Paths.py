class Solution:
    def _binaryTreePaths(self, root, curr, paths):
        if not root:
            return root
        curr.append(str(root.val))
        if not root.left and not root.right:
            paths.append('->'.join(curr))
        else:
            self._binaryTreePaths(root.left, curr, paths)
            self._binaryTreePaths(root.right, curr, paths)
        del curr[-1]
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        paths = []
        self._binaryTreePaths(root, [], paths)
        return paths
        
