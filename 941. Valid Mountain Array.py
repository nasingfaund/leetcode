class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        
        i = 0
        
        while i < n -1 and arr[i+1] > arr[i]:
            i += 1
            
        if i == n -1 or i == 0:
            return False
        
        while i < n -1 and arr[i+1] < arr[i]:
            i+=1
        
        if i != n -1:
            return False
        
        return True
        
