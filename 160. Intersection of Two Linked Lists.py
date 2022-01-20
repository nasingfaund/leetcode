# complexity O(m+n), space O(1)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        p, q = headA, headB

        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA 

        return p
    
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return
        p = headA
        q = headB
        
        while p or q:
            if p == q:
                return p
            
            p  = p.next if p else headB
            q = q.next if q else headA
    
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        s = set()
        while headA:
            s.add(headA)
            headA = headA.next

        while headB:
            if headB in s:
                return headB
            headB = headB.next
        return None
