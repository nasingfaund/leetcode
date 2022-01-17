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
        
