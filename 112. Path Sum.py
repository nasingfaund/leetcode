# dfs has O(V + E), this is a tree so E = V - 1 (undirected, acyclic, connected graph) => O(V + V - 1) => O(2*V - 1) => O(V) 
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]

        while stack:
            root, value = stack.pop()
            if value == targetSum and not root.left and not root.right:
                return True
            if root.left:
                stack.append((root.left, value + root.left.val))
            if root.right:
                stack.append((root.right, value + root.right.val))
        return False

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if root.val == targetSum and not root.left and not root.right:
            return True

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    
# bfs 
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        queue = deque([(root, root.val)])
        
        while queue:
            for _ in range(len(queue)):
                node, value = queue.popleft()
                if value == targetSum and not node.left and not node.right:
                    return True
                if node.left:
                    queue.append((node.left, node.left.val + value ))
                if node.right:
                    queue.append((node.right, node.right.val + value))
        return False
