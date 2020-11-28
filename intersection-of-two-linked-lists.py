# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        cur1, cur2 = headA, headB

        len1 = len2 = 0

        while cur1:
            len1 += 1
            cur1 = cur1.next

        while cur2:
            len2 += 1
            cur2 = cur2.next

        if cur1 is not cur2:
            return

        cur1, cur2 = headA, headB

        diff = abs(len1 - len2)
        m = max(len1, len2)

        for _ in range(diff):
            if m == len1:
                cur1 = cur1.next
            else:
                cur2 = cur2.next

        while cur1 and cur2:
            if cur1 is cur2:
                return cur1
            cur1 = cur1.next
            cur2 = cur2.next
        return
