class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = curr_head = ListNode(None)
        
        while l1 or l2:
            if not l2:
                while l1:
                    curr.next = l1
                    curr = curr.next
                    l1 = l1.next
            elif not l1:
                while l2:
                    curr.next = l2
                    curr = curr.next
                    l2 = l2.next
            else:
                minv = min(l1.val, l2.val)
                print(minv)
                if minv == l1.val and minv == l2.val:
                    curr.next = ListNode(minv)
                    curr.next.next = ListNode(minv)
                    l1 = l1.next
                    l2 = l2.next
                    curr = curr.next.next
                elif minv == l1.val:
                    curr.next= ListNode(minv)
                    l1 = l1.next
                    curr = curr.next
                elif minv == l2.val:
                    curr.next= ListNode(minv)
                    l2 = l2.next
                    curr = curr.next
        return curr_head.next
