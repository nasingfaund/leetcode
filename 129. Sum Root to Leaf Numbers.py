class Solution:
    def _sumNumers(self, root, path_sum):
        if not root:
            return 0
        path_sum = path_sum*10 + root.val
        if not root.left and not root.right:
            return path_sum
        return self._sumNumers(root.left, path_sum) + self._sumNumers(root.right, path_sum)
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self._sumNumers(root, 0)

      
# (Iterative DFS - preorder)
 class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        queue, total_sum = deque([(root, 0)]), 0
        while queue:
            root, cur = queue.pop()
            cur = cur * 10 + root.val
            if not root.left and not root.right: 
                total_sum += cur
            if root.right: 
                queue.append((root.right, cur))
            if root.left: 
                queue.append((root.left, cur))
        return total_sum
        
# silly solution
class Solution:
    def dfs(self, root, curr, values):
        if not root:
            return 
        if not root.left and not root.right:
            values.append(curr)
        if root.left:
            self.dfs(root.left, curr*10 + root.left.val, values)
        if root.right:
            self.dfs(root.right, curr*10 + root.right.val, values)
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        values = []
        
        self.dfs(root, root.val, values)
        return sum(values)
