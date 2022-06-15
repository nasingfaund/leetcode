class Solution:
    def dfs(self, root, adict, level):
        if not root:
            return 
        adict[level].append(root.val)
        
        self.dfs(root.left, adict, level+1)
        self.dfs(root.right, adict, level + 1)
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        adict = defaultdict(list)
        self.dfs(root, adict, 0)
        return adict.values()
   
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        result = []
        queue = deque([root])
        
        while queue:
            curr_level = []
            for _ in range(len(queue)):
                root = queue.popleft()
                curr_level.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            result.append(curr_level)
        return result
