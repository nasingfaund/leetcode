class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return root
        queue = deque()
        queue.append(root)
        leftToRight = True
        while queue:
            curr = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if leftToRight:
                    curr.append(node.val)
                else:
                    curr.appendleft(node.val)
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(list(curr))
            leftToRight = not leftToRight
        return result
