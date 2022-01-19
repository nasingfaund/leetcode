class Solution:
    def insertionSortList(self, head):
        curr = head
        while curr:
            runner = head
            while runner != curr:
                if runner.val > curr.val: 
                    runner.val, curr.val = curr.val, runner.val
                runner = runner.next
            curr = curr.next
        return head
