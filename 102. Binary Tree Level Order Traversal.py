# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        result = []
        queue = [root]
        while queue:
            queue_len = len(queue)
            curr_level = []
            for _ in range(queue_len):
                root = queue.pop(0)
                curr_level.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            result.append(curr_level)
        return result
        
