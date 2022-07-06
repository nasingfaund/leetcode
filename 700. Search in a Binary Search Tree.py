class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = root
        
        while temp:
            if val == temp.val:
                return temp
            elif val > temp.val:
                temp = temp.right
            elif val < temp.val:
                temp = temp.left

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return 
        if root.val == val:
            return root
        
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
