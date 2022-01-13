class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        passed = []
        while head:
            if head in passed:
                return passed[passed.index(head)]
            passed.append(head)
            head = head.next
        
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                temp = head
                while temp != slow:
                    temp = temp.next
                    slow  = slow.next
                return temp
        
        
        
