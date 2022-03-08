class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        result = deque()
        queue = deque()
        queue.append(root)
        while queue:
            curr = []
            for _ in range(len(queue)):
                root = queue.popleft()
                curr.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            result.appendleft(curr)

        return result
