# Complexity O(n), Space O(1)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp = head
        
        while temp and temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
            
        return head
    
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next.val  else head
            
                
