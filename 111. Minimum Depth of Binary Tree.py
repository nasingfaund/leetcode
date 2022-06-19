class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        min_level = 0
        while queue:
            min_level +=1
            for _ in range(len(queue)):
                root = queue.popleft()
                if not root.left and not root.right:
                    return min_level
                
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                    
        return -1

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return float('inf')
            if not root.left and not root.right:
                return 1
            left = dfs(root.left)
            right = dfs(root.right)
            
            return min(left, right) + 1
            
        return dfs(root) if root else 0
