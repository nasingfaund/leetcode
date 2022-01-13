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
            
        
