#dummy 

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odds = []
        even = []
        temp = head
        i = 0
        while temp:
            if i % 2 == 1:
                odds.append(temp)
            else:
                even.append(temp)
            temp = temp.next
            i += 1
        curr = curr_head = ListNode(None)
        for e in even:
            curr.next = ListNode(e.val)
            curr = curr.next
        for o in odds:
            curr.next = ListNode(o.val)
            curr = curr.next
    
       
        return curr_head.next

        
        
 class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

        
        
