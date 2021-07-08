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
            
