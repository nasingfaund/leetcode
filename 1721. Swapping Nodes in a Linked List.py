class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length +=1
        
        first = head
        for _ in range(k-1):
            first = first.next
        second = head
        for _ in range(length - k):
            second = second.next
            
        temp = first.val
        first.val = second.val
        second.val = temp
        
        return head

# swapping node values    
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        first = last = head
        for _ in range(k-1):
            first = first.next
            
        node = first
        while node.next:
            node = node.next
            last = last.next
        
        temp = first.val
        first.val = last.val
        last.val = temp
        
        return head
    
# two pointers
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy =  pre_right = pre_left = ListNode(-1)
        dummy.next = pre_right.next = pre_left.next =  head
        
        right = left = head
        for i in range(k-1):
            pre_left = left
            left = left.next

        temp = left

        while temp.next:
            pre_right = right
            right = right.next
            temp = temp.next

        if left == right:
            return head

        pre_left.next, pre_right.next = right, left
        left.next, right.next = right.next, left.next
        return dummy.next 
