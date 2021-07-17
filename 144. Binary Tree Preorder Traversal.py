class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        

        
        
 # iterative solution
 class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        
        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
        return result
