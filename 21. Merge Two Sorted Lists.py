class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        
        dummy_head = curr = ListNode(-1)
        while l1 and l2:
            if l1.val >= l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
            
        curr.next = l1 or l2
        return dummy_head.next      
        
    
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


# 06-02-2022
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = curr = ListNode(-1)
        
        while list1 or list2:
            if not list1:
                curr.next = ListNode(list2.val)
                curr = curr.next
                list2 = list2.next
                continue
            if not list2:
                curr.next = ListNode(list1.val)
                curr = curr.next
                list1 = list1.next
                continue
                
            if list1.val >= list2.val:
                curr.next= ListNode(list2.val)
                curr = curr.next
                list2 = list2.next
            else:
                curr.next= ListNode(list1.val)
                curr = curr.next
                list1 = list1.next
            
        return dummy_head.next
