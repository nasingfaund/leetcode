
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
            
