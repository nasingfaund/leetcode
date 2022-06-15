# dfs
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        
        if if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
                
# dfs iterative        
 class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        
        while stack:
            p, q = stack.pop()
            if not p and q or not q and p:
                return False
            
            if p and q and p.val != q.val:
                return False
            
            if p and q:
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))

        return True
           
# bfs
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])
        while queue:
            p, q = queue.popleft()
            
            if not p and q or not q and p:
                return False
            
            if p and q and p.val != q.val:
                return False
            
            if p and q:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))

        return True
            
