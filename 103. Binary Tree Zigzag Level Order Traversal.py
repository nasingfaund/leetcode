# improved
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
    
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        
        result = []
        is_revert = False
        while queue:
            if is_revert:
                result.append(list(reversed([node.val for node in queue])))
                is_revert = False
            else:
                result.append([node.val for node in queue])
                is_revert = True
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        
        result = []
        is_revert = True
        while queue:
            d = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
                if is_revert:
                    d.append(node.val)
                else:
                    d.appendleft(node.val)
                    
            result.append(list(d))
            is_revert = not is_revert
        return result
                    
