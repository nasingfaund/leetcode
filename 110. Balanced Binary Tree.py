class Solution:
    def dfs(self, root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        if left == -1:
            return -1
        right = self.dfs(root.right)
        if right == -1:
            return -1
        
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) != -1

# iterative, based on post order traversal
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        # how about storing parent node? Does not work
        stack = []
        last_visited = None
        adict = defaultdict(int)
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                peek_node = stack[-1]
                if peek_node.right and last_visited != peek_node.right:
                    root  = peek_node.right
                else:
                    print(peek_node.val)
                    l = adict[peek_node.left]
                    r = adict[peek_node.right]
                    if abs(l - r) > 1:
                        return False
                    adict[peek_node] =  max(l, r) + 1 
                    
                    last_visited =  stack.pop()
        return True
