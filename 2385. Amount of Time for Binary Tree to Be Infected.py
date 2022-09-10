class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        def dfs(root):
            graph[root].append(root)
            if root.left:
                graph[root].append(root.left)
                graph[root.left].append(root)
                dfs(root.left)
            if root.right:
                graph[root].append(root.right)
                graph[root.right].append(root)
                dfs(root.right)
                
        dfs(root)
        
        start_node = next((node for node in graph if node.val == start), None)
        if not start_node:
            raise
        
        visited = {start_node}
        queue = deque([(start_node, 0)])
        ans = 0
        while queue:
            node, depth = queue.popleft()
            ans = max(depth, ans)
            
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    queue.append((n, depth +1))
        return ans
            
