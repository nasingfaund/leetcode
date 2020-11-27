# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        last = None
        while curr != None:
            n = ListNode(curr.val)
            n.next = last

            last = n

            curr = curr.next
        return last

