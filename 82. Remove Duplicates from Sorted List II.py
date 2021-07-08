class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head

        curr = head
        res = res_head = ListNode(None)
        while curr:
            if curr.next and curr.val == curr.next.val:
                pred = curr
                while curr.next and  pred.val == curr.next.val:
                    curr = curr.next
            else:
                res.next = ListNode(curr.val)
                res = res.next
                
            curr = curr.next

        return res_head.next
