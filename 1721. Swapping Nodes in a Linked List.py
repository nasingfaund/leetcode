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
