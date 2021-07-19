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
