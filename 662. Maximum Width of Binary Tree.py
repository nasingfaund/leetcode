class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        res = defaultdict(list)

        def dfs(level, p, root):
            if not root:
                return p

            res[level].append(p)
            dfs(level + 1, 2 * p, root.left)
            dfs(level + 1, 2 * p + 1, root.right)

        dfs(0, 0, root)
        return max(max(a) - min(a) + 1 for a in res.values())

    
 class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        queue = deque([[root, 1]])
        res = 0
        
        while queue:
            nodes = []
            for _ in range(len(queue)):
                node, num = queue.popleft()
                nodes.append(num)
                if node.left:
                    queue.append([node.left, 2 * num])
                if node.right:
                    queue.append([node.right, 2 * num + 1])
            res = max(nodes[-1] - nodes[0] + 1, res)
        return res
