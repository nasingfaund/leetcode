class Solution:
    def rangeSumBST(self, root, L, H):
        return  ((root.val if root.val >= L and root.val <= H else 0) + self.rangeSumBST(root.left, L, H) + self.rangeSumBST(root.right, L, H)) if root else 0
