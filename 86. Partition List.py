class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less =curr_less = ListNode(-1)
        greater = curr_greater =  ListNode(-1)
        
        while head:
            if head.val < x:
                curr_less.next = ListNode(head.val)
                curr_less = curr_less.next
            else:
                curr_greater.next = ListNode(head.val)
                curr_greater = curr_greater.next
                
            head = head.next
            
        
        curr_less.next = greater.next
        
        return less.next
        
