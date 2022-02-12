class Solution:
    def reverseBetween(self, head: Optional[ListNode], p: int, q: int) -> Optional[ListNode]:
        if p == q:
            return head

        current, previous = head, None
        for i in range(p-1):
            previous = current
            current = current.next

        last_node_of_first_part = previous
        last_node_of_sub_list = current
        
        temp = None  
        for i in range(q-p+1):
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        if last_node_of_first_part:
            last_node_of_first_part.next = previous
        else:
            head = previous

        last_node_of_sub_list.next = current
        return head
    
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
            
        
