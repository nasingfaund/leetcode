class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        curry = 0
        for i in range(len(digits)-1, -1, -1):
            val = digits[i] + 1
            if val == 10:
                digits[i] = 0
                curry = 1
            else:
                digits[i] = val
                curry = 0
                break
        if curry:
            digits = [1] + digits
        return digits
            
        
