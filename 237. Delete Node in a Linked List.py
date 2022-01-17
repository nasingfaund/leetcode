# clever solution
class Solution:
    def deleteNode(self, node):
        if not node or not node.next:
            return False
        
        node.val = node.next.val
        node.next = node.next.next

        
# stupid solution 
class Solution:
    def deleteNode(self, node):
        temp = node
        while temp.next:
            prev = temp
            value = temp.val
            temp.val = temp.next.val
            temp.next.val = value
            
            temp = temp.next
            
        prev.next = None
            
        
