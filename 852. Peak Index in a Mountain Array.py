class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        first = 0
        second = len(arr)
        while first< second:
            middle = (first  + second) // 2
            
            if arr[middle] < arr[middle + 1]:
                first = middle + 1
            else:
                second = middle
        return first
        
