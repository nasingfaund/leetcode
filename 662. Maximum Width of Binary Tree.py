class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        res = defaultdict(list)

        def f(level, p, root):
            if not root:
                return p
            
            res[level].append(p)
            left = f(level + 1, 2 * p, root.left)
            right = f(level + 1, 2 * p + 1, root.right)
        
        f(0, 0, root)
        return max(max(a) - min(a) + 1 for a in res.values())
