class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(root, parent=None):
            if root:
                root.parent = parent
                dfs(root.left, root)
                dfs(root.right, root)
        
        dfs(root)
        result = []
        
        queue = deque([(target, 0)])
        visited = {target}
        
        while queue:
            if queue[0][1] == k:
                return [node.val for node, d in queue]
            
            node, d = queue.popleft()
            
            for n in (node.left, node.right, node.parent):
                if n and n not in visited:
                    visited.add(n)
                    queue.append((n, d+1))
        return []
            
        
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {root: None}
        def dfs(root, parent=None):
            if root:
                parents[root.left] = root
                parents[root.right] = root
                
                dfs(root.left, root)
                dfs(root.right, root)
                
        dfs(root)
        result = []
        
        queue = deque([(target, 0)])
        visited = {target}
        
        while queue:
            if queue[0][1] == k:
                return [node.val for node, d in queue]
            
            node, d = queue.popleft()
            
            for n in (node.left, node.right, parents[node]):
                if n and n not in visited:
                    visited.add(n)
                    queue.append((n, d+1))
        return []
            
        
