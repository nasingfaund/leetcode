# true bfs
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        queue = deque([root])
        max_depth = 0
        while queue:
            max_depth += 1
            for _ in range(len(queue)):
                root = queue.popleft()
                for node in root.children:
                    queue.append(node)
        return max_depth
    
# bfs 
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        visited = set()
        max_depth = 0
        while queue:
            root, depth = queue.popleft()
            visited.add(root)
            max_depth = max(max_depth, depth)
            
            for node in root.children:
                if node not in visited:
                    queue.append((node, depth + 1))
        return max_depth
    
# dfs itertive
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        visited = set()
        max_depth = 0
        while stack:
            root, depth = stack.pop()
            visited.add(root)
            max_depth = max(max_depth, depth)
            
            for node in root.children:
                if node not in visited:
                    stack.append((node, depth + 1))
        return max_depth
    
class Solution:
    def dfs(self, root, visited):
        visited.add(root)
        ans = 1
        for node in root.children:
            if node not in visited:
                ans = max(self.dfs(node, visited) + 1, ans)
        return ans
        
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        return self.dfs(root, set())
    

# silly use of recursion
class Solution:
    maximum = 1
    def dfs(self, root, visited, depth):
        # print(depth)
        visited.add(root)
        for node in root.children:
            if node not in visited:
                ans = self.dfs(node, visited, depth + 1) # sub ans
                self.maximum = max(self.maximum, ans)
        return depth
        
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        self.dfs(root, set(), 1)
        return self.maximum
        
        
