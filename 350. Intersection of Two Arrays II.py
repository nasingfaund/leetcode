class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1.sort()
        nums2.sort()
        
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i+=1
                j +=1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result
      
      
 class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        adict = defaultdict(int)
        for num in nums1:
            adict[num] += 1
        for num in nums2:
            if adict[num] > 0:
                result.append(num)
                adict[num] -= 1
            
        return result
