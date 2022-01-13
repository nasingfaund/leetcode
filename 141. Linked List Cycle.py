class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        def _hasCycle(head: ListNode, seen) -> bool:
            if not head:
                return False
            if head in seen:
                return True

            return _hasCycle(head.next, seen + [head])
        return _hasCycle(head, [])
        

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        temp = head
        seen = set()
        while temp.next:
            if temp in seen:
                return True
            seen.add(temp)
            temp = temp.next
        return False
        

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False
            
        
