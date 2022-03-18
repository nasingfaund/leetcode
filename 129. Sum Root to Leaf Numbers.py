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
        
