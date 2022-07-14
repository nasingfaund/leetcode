class Solution:
    def getMin(self, root):
        temp  = root
        while temp.left:
            temp = temp.left
        return temp
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return 
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            min_value = self.getMin(root.right)
            root.val = min_value.val
            root.right = self.deleteNode(root.right, root.val)

        return root
