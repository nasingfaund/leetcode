class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        
        queue = deque([root])
        while queue:
            result.append(queue[0].val)
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.right:
                    queue.append(curr.right)                
                if curr.left:
                    queue.append(curr.left)

        return result
    
    
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(root, depth):
            if not root:
                return 
            
            if depth == len(result):
                result.append(root.val)
                
            dfs(root.right, depth + 1)  # Go right side first
            dfs(root.left, depth + 1)
            
        dfs(root, 0)
        return result
