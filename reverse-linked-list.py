# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(self, head: ListNode) -> ListNode:
    curr = head
    last = None
    while curr != None:
        n = ListNode(curr.val)
        n.next = last

        last = n

        curr = curr.next
    return last

def reverse_list(head):
    new_head = None
    while head != None:
        tmp = head.next
        head.next = new_head

        new_head = head
        head = tmp

    return new_head
