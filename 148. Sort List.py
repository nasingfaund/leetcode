# time execution limit
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        curr = curr_head = head
        while curr:
            runner = curr
            while runner:
                if runner.val < curr.val:
                    temp = runner.val
                    runner.val = curr.val
                    curr.val = temp
                runner = runner.next
            curr = curr.next
        return curr_head
        
        
#dummy solution
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        res = []
        temp = head
        curr = curr_head = ListNode(None)
        
        while temp:
            res.append(temp.val)
            temp = temp.next
        res = list(sorted(res))
        for i in res:
            curr.next = ListNode(i)
            curr = curr.next
        return curr_head.next
    
            
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        mid = self.get_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def get_mid(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        return mid
    
    def merge(self, left, right):
        curr = curr_head = ListNode(None)
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left or right
        return curr_head.next
            
        
