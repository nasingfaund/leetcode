from copy import deepcopy


def reverseList(head):
    new_head = None
    head = deepcopy(head)
    while head:
        tmp = head.next
        head.next = new_head
        new_head = head
        head = tmp
    return new_head


def get_length(head):
    temp = head
    length = 0
    while temp:
        length += 1
        temp = temp.next
    return length


def reorderList(head) -> None:
    """
    Do not return anything, modify head in-place instead.
    """

    reversed_head = reverseList(head)
    length = get_length(head)
    i = 0
    curr = curr_head = head
    while head and i < length:
        if i % 2 == 1:
            tmp = curr.next
            rev_head = reversed_head.next
            reversed_head.next = None
            curr.next = reversed_head
            reversed_head.next = tmp
            reversed_head = rev_head
            if i + 1 == length:
                curr = curr.next
            else:
                curr = curr.next.next
        i += 1
    curr.next = None
    return curr_head


print_list(reorderList(head))
