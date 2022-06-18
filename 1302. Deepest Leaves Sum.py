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
        return sum(adict[max(adict.keys())])   
    
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.deepest = 0
        def dfs(root, depth):
            if not root:
                return 0
            if not root.left and not root.right:
                if depth == self.deepest:
                    self.res += root.val
                elif depth > self.deepest:
                    self.res = root.val 
                    self.deepest = depth
            left = dfs(root.left, depth + 1)
            right = dfs(root.right, depth + 1)
            return self.res
        return dfs(root, 0)
