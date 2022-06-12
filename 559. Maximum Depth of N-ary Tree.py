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
        
        
