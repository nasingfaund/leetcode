class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(root, node, path):
            if not root:
                return 
            if root == node:
                return path + [node]
            return find(root.left, node, path + [root]) or find(root.right, node, path + [root])
                
                
        first =  find(root, p, [])
        second = find(root,q, [])

        for i in range(min(len(first), len(second))):
            if i > 0 and first[i] != second[i]:
                return first[i-1]
            if i == min(len(first), len(second)) - 1:
                return first[i]
            
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return 
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if not left or not right:
            return left or right
        
        return root
        
