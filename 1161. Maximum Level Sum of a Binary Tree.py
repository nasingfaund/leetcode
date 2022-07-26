class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        result = defaultdict(int)
        
        def dfs(root, level):
            
            if not root:
                return
            result[level+1] += root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        dfs(root, 0)
        return max(result, key=result.get)
    
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        result = defaultdict(int)
        
        stack = [[root, 1]]

        while stack:
            node, level = stack.pop()
            result[level] += node.val
            if node.left:
                stack.append([node.left, level + 1])
            if node.right:
                stack.append([node.right, level + 1])
        print(result)
        return max(result, key=result.get)
