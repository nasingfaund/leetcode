class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
        
        
        
        
# BFS
class Solution:
    def invertTree2(self, root):
        queue = collections.deque([(root)])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

    
    
# DFS
class Solution:
    def invertTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.right, node.left 
        return root
        
