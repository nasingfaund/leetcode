class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return root
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            queue_len = len(queue)
            curr_sum = 0.0
            for _ in range(queue_len):
                root = queue.popleft()
                curr_sum += root.val
                
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                    
            result.append(curr_sum/queue_len)
        return result
        
