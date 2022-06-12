# dfs iterative
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        stack = [(root, 1)]

        max_depth = 0
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return max_depth
# dfs
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right) +1)
        
# bfs (multilevel)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        max_depth = 0
        
        while queue:
            max_depth += 1
            for _ in range(len(queue)):
                root = queue.popleft()
                
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                    
        return max_depth
