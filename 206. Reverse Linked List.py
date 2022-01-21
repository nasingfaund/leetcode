# Complexity O(n), space O(n)
class Solution:
    def reverseList(self, head):
        new_head = None
        
        while head:
            temp = head.next
            
            head.next = new_head
            new_head = head
            
            head = temp

        return new_head

    
class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node
