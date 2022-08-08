class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        orig = x
        back = 0
        while x > 0:
            back = (back * 10) + x % 10
            x //= 10
        return back == orig
