class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode(0)
        while l1 or l2:
            if not l1:
                curr.next = l2
                return head.next
            if not l2:
                curr.next = l1
                return head.next
            if l1.val >= l2.val:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
            elif l1.val < l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
        return head.next

    
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


