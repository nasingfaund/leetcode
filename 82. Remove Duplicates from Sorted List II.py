class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = ListNode(None)

        curr = head
        res = res_head = ListNode(None)
        while curr and curr.next:
            if curr.val == curr.next.val:
                pred = curr
                while pred.val == curr.next.val:
                    curr = curr.next
            else:
                res.next = ListNode(curr.val)
                res = res.next
            curr = curr.next

        return res_head.next
