class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        adict = defaultdict(list)
        def dfs(root, depth):
            if not root:
                return 0
            if not root.left and not root.right:
                adict[depth].append(root.val)
                
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        return sum(adict.get(max(adict.keys())))    
