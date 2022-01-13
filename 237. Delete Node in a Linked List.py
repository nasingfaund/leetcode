# clever solution
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        
        """
        temp = node
        temp.val = temp.next.val

        temp.next = temp.next.next


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        
        """
        temp = node
        while temp.next:
            prev = temp
            value = temp.val
            temp.val = temp.next.val
            temp.next.val = value
            
            temp = temp.next
            
        prev.next = None
            
        
