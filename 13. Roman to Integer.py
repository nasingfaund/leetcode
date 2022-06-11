# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        duo = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        i = 0
        result = 0
        while i < len(s):
            if value:=duo.get(s[i:i + 2]):
                result += value
                i += 2
            else:
                result += mapping.get(s[i])
                i += 1
        return result

                
            
        
