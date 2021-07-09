class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        passed = []
        while head:
            if head in passed:
                return passed[passed.index(head)]
            passed.append(head)
            head = head.next
        
