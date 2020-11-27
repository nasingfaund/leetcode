"""
https://leetcode.com/problems/middle-of-the-linked-list/solution/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        curr = head

        while curr != None:
            length +=1
            curr = curr.next

        middle = length // 2

        c = head
        for _ in range(middle):
            c = c.next

        return c

        
