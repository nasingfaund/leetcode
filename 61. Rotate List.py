class Solution:
    def revertList(self, head):
        dummy_head  = None 
        curr = head
        while curr:
            node = ListNode(curr.val)
            node.next = dummy_head
            dummy_head = node
            
            curr = curr.next
        return dummy_head
    
    def get_length(self, head):
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length +=1
        return length
        
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        
        reverted_list = temp = self.revertList(head)
        length = self.get_length(head)
        
        k = k % length
        while k > 0:
            if not temp:
                temp = reverted_list
            node = ListNode(temp.val)
            node.next = head
            head = node
            
            temp = temp.next
            k-=1
            
        curr = head
        while length - 1 > 0 and curr:
            curr = curr.next
            length -=1
            
        if curr:
            curr.next = None
        
        return head
