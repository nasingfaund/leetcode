# naive solution
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder(root):
            if not root:
                return []
            return  inorder(root.left) +[root.val]+ inorder(root.right)
        
        values = inorder(root)
        print(values)
        return values[k-1]
        
