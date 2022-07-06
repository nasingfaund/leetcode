class Solution:
    def isValidBST(self, root):
        output = self.inOrder(root)
        
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False

        return True

    def inOrder(self, root):
        if root is None:
            return []
        
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)
    
class Solution:
    def isValidBST(self, root):
        def dfs(node, low, high):
            if not node: 
                return True
            if not low < node.val < high: 
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root, -float("inf"), float("inf"))
