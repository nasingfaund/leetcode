class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        counter = 0
        stack = []
        p = res = head
        while counter < left-1:
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
            
        
