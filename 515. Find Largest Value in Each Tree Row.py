class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = defaultdict(list)

        def dfs(root, level):

            if not root:
                return
            result[level+1].append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        dfs(root, 0)
        return [max(val) for val in result.values()]
      
      
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = defaultdict(int)

        def dfs(root, level):

            if not root:
                return
            result[level] = max(result[level], root.val) if level in result else root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        dfs(root, 0)
        return result.values()
