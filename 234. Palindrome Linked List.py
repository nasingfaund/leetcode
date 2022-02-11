# Follow up: Could you do it in O(n) time and O(1) space? Yes, with accurate reverse part
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        rev_head = None
        temp  = slow
        while temp:
            _next = temp.next
            temp.next  = rev_head
            rev_head = temp
            temp = _next

        while head!=slow:
            if head.val != rev_head.val:
                return False
            head = head.next
            rev_head = rev_head.next
        return True

# stack
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next
            
        while head:
            val = stack.pop()
            if val != head.val:
                return False
            head = head.next
        return True
    
# No need to put in stack all nodes, half is enough
class Solution:
    def isPalindrome(self, head):
        slow = fast = head
        stack  = []
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next
            
        while slow:
            top = stack.pop()
            if top  != slow.val:
                return False
            slow = slow.next
        return True
            
            
# with revert
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev_head  = None
        temp = head
        while temp:
            node = ListNode(temp.val)
            node.next = rev_head
            rev_head = node
            
            temp = temp.next
            
        while head:
            if head.val!=rev_head.val:
                return False
            
            head = head.next
            rev_head = rev_head.next
            
        return True
            
