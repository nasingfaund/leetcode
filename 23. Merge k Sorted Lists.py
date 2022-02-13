# brute force
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        dummy_head = curr = ListNode(-1)
        for alist in lists:
            while alist:
                nodes.append(alist.val)
                alist  = alist.next
        for x in sorted(nodes):
            curr.next = ListNode(x)
            curr = curr.next
        return dummy_head.next
        
        
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy_head = curr = ListNode(-1)
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
                
        curr.next = list1 or list2
        
        return dummy_head.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        alist = lists[0]
        for i in range(1, len(lists)):
            alist = self.mergeTwoLists(alist, lists[i])
        
        return alist
        
