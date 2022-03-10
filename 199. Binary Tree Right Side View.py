class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        
        queue = deque()
        queue.append(root)
        while queue:
            result.append(queue[0].val)
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.right:
                    queue.append(curr.right)                
                if curr.left:
                    queue.append(curr.left)

        return result
