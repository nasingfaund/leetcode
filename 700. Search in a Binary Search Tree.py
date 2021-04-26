# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        temp = root
        while temp:
            if val == temp.val:
                return temp

            if val > temp.val:
                temp = temp.right
            else:
                temp = temp.left

        return None


        
