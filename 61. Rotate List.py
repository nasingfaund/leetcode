class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        temp = head
        length = 1
        while temp.next:
            length +=1
            temp = temp.next
            
        temp.next = head
        
        it = k % length 
        
        for i in range(length-it):
            temp = temp.next
            
        head = temp.next
        temp.next = None
        return head
    
    
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        
        tail = head
        n = 1
        
        while tail.next:
            tail = tail.next
            n += 1
            
        if k % n == 0:
            return head
        
        middle = head
        for i in range(n - k%n-1):
            middle = middle.next
            
        new_head = middle.next
        tail.next = head
        middle.next = None
        return new_head
        
    
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        tail = head
        length = 1
        while tail.next:
            length +=1
            tail = tail.next
            
        tail.next = head
        
        it = k % length 
        
        for i in range(length-it):
            tail = tail.next
            
        head = tail.next
        tail.next = None
        return head
            
