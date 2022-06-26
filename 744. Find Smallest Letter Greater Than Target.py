class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        first  = 0 
        second = len(letters)
        while first < second:
            middle = (first + second) // 2
            
            if target >= letters[middle]:
                first = middle + 1
            else:
                second = middle
        
        return letters[first] if first < len(letters) else letters[0]
        
