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
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: 
                slow2 = head
                while slow2!=slow:
                    slow = slow.next
                    slow2 = slow2.next
                return slow 
        
        
