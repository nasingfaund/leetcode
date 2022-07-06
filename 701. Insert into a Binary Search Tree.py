class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root
    
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        temp = root
        while temp:
            if val > temp.val:
                if not temp.right:
                    temp.right = TreeNode(val)
                    return root
                else:
                    temp = temp.right
            else:
                if not temp.left:
                    temp.left = TreeNode(val)
                    return root
                else:
                    temp = temp.left
