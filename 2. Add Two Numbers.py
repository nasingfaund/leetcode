# dirty but works
class Solution:
    def append_zeros(self, l1, l2):
        l1_temp = l1
        l2_temp = l2
        while l1_temp or l2_temp:
            if l1_temp and not l1_temp.next:
                shorter = l1
                break
            elif l2_temp and not l2_temp.next:
                shorter = l2
                break
                
            l1_temp = l1_temp.next
            l2_temp = l2_temp.next
            
        longest = curr_longest = l2 if shorter == l1 else l1
        shorter = curr_shorter = l1 if longest == l2 else l2
        while curr_longest:
            if not curr_shorter.next:
                curr_shorter.next = ListNode(0)
                
            curr_longest = curr_longest.next
            curr_shorter = curr_shorter.next
        return longest, shorter
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
       
        l1, l2 =  self.append_zeros(l1, l2)
        
        result = curr = ListNode(-1)
        rem = 0
        while l1 and l2:
            value  = l1.val + l2.val + rem
            rem = value // 10
            curr.next = ListNode(value % 10)
            curr = curr.next
            
            l1 = l1.next
            l2 = l2.next
        if rem:
            curr.next = ListNode(rem)
            
        return result.next
    
    
    
    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = curr = ListNode(-1)
        carry = 0
        p = l1
        q  = l2
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            result_sum = carry + x + y
            carry = result_sum // 10
            curr.next= ListNode(result_sum % 10)
            curr = curr.next
#             carry, val = divmod(carry + x + y, 10)
#             curr.next= ListNode(val)
            if p: p = p.next
            if q:q = q.next
                
        if carry > 0:
            curr.next = ListNode(carry)
            
        return dummy_head.next
        
        
        
# last written (took more than 1 hour)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_l1, curr_l2 = l1, l2
        
        while curr_l1.next and curr_l2.next:
            curr_l1 = curr_l1.next
            curr_l2 = curr_l2.next
            
        while curr_l1 or curr_l2:
            node = ListNode(0)
            
            if curr_l1.next and curr_l2:
                curr_l2.next = node
            elif curr_l2.next and curr_l1:
                curr_l1.next = node
            
            curr_l2 = curr_l2.next
            curr_l1 = curr_l1.next
        
        dummy_head = curr = ListNode(0)
        curry = 0
        while l1 and l2:
            res = l1.val + l2.val + curry
            if res >= 10:
                curry = res // 10
            else:
                curry = 0
            curr.next = ListNode(res % 10)
            curr = curr.next

            l1 = l1.next 
            l2 = l2.next
        
        if curry:
            curr.next  = ListNode(curry)

                
        return dummy_head.next
    
        
        
