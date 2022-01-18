class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        p, q = headA, headB

        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA 

        return p

    
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
