# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        head = root
        if root is None:
            return TreeNode(val)

        while root:
            if val > head.val:
                if head.right is None:
                    head.right = TreeNode(val)
                    return root
                else:
                    head = head.right
            elif val < head.val:
                if head.left is None:
                    head.left = TreeNode(val)
                    return root
                else:
                    head = head.left
        return root

        # Definition for a binary tree node.

# Recursive
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
        
