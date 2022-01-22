class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        counter = 0
        stack = []
        p = res = head
        while counter < left:
            counter += 1
            p = p.next
        q = p    
        while q and left <= right:
            stack.append(q.val)
            q = q.next
            left +=1
            
        while stack and p != q:
            val = stack.pop()
            p.val = val
            p = p.next
            
        return res
    
    def get_length(self, head):
        temp = head
        length =  0
        while temp:
            length += 1
            temp = temp.next
        return length

       
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left  = right =  0
        
        length = self.get_length(head)
        i = 0
        
        while i < length // k:
            for _ in range(k-1):
                right +=1
                
            head = self.reverseBetween(head, left, right)
            
            right = right +1
            left = right
            i+=1
            
        return head
