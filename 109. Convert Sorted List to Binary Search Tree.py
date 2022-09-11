class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def build_bst(head, tail):
            slow, fast = head, head
            if head == tail:
                return None
            
            while fast!=tail and fast.next!=tail:
                slow = slow.next
                fast = fast.next.next
                
            n = TreeNode(slow.val)
            n.left = build_bst(head, slow)
            n.right = build_bst(slow.next, tail)
            return n
        
        if not head:
            return None
                
        return build_bst(head, None)
