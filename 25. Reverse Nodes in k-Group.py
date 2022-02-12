# after educative https://www.educative.io/courses/grokking-the-coding-interview/RMZylvkGznR
class Solution:
    def reverseBetween(self, head: ListNode, p: int, q: int) -> ListNode:
        if p == q:
            return head

        current, previous = head, None
        for i in range(p - 1):
            previous = current
            current = current.next

        last_node_of_first_part = previous
        last_node_of_sub_list = current
        
        for i in range(q - p + 1):
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

    def get_length(self, head):
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        return length

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = 1
        q = k
        length = self.get_length(head)

        it = length // k
        for i in range(it):
            head = self.reverseBetween(head, p, q)
            p +=k
            q += k

        return head


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
