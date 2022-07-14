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
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k-=1 
            if not k:
                return root.val
            root = root.right
            
        
