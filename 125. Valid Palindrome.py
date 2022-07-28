class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized_string = ''.join(c for c in s if c not in string.punctuation)
        sanitized_string = sanitized_string.lower().replace(' ', '')
        print(sanitized_string)
        return sanitized_string == sanitized_string[::-1]
        
