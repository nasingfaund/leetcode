# with modifing the array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        def combine(a,b):
            if not a or not b:
                return a or b
            if a[0] >= b[0]:
                return [b[0]] + combine(a, b[1:])
            return [a[0]] + combine(a[1:], b)
        a = list(nums1[:m])
        b = list(nums2[:n])
        nums1[:] = combine(a, b)[:] 
    
    
from heapq import merge
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a = list(nums1[:m])
        b = list(nums2[:n])
        nums1[:] = list(merge(a, b))[:] 
