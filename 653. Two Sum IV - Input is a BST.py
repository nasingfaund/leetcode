class Solution:
    def dfs(self, root):
        return self.dfs(root.left) + [root.val] + self.dfs(root.right) if root else []
    
    def findTarget(self, root: TreeNode, k: int) -> bool:
        inorder_trav = self.dfs(root)
        first = 0
        last = len(inorder_trav) - 1
        while first < last:
            sum_elem = inorder_trav[first] + inorder_trav[last]
            if sum_elem==k:
                return True
            elif sum_elem > k:
                last -=1
            else:
                first +=1
        return False
        
