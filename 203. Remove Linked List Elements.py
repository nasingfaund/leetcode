# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head, val):
        new_head = curr = ListNode()
        new_head.next = head
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return new_head.next
    
class Solution:
    def removeElements(self, head, val):
        new_head = curr = ListNode()
        while head:
            if head.val != val:
                curr.next = ListNode(head.val)
                curr = curr.next
                
            head = head.next
            
        return new_head.next

class Solution:
    def removeElements(self, head, val):
        if head is None:
            return head

        new_head = deepcopy(head)

        while new_head and new_head.val == val:
            new_head = new_head.next

        temp = new_head

        if temp is None:
            return temp

        # in the middle
        while temp and temp.next != None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return new_head

