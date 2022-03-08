class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
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
