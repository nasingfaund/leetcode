# https://assets.leetcode.com/users/images/5f84e242-69cb-4dc4-97ef-f492465f46f3_1595418237.69286.png
        
# https://www.youtube.com/watch?v=L-Wzglnm4dM        
class Solution:
    def binpow(self, a, n):
        if n == 0:
            return 1
        if n == 1:
            return a
        tmp = self.myPow(a, n // 2)
        result = tmp * tmp
        if n % 2 == 1:
            result *= a
        return result

        
    def myPow(self, a, n):
        return 1/self.binpow(a, abs(n)) if n < 0 else self.binpow(a, n) 
        
        
 class Solution:
    def binpow(self, a, n):
        a, b = a, n
        result = 1
        while b > 0:
            if b % 2 == 1:
                result *= a
            a *= a
            b //= 2
        return result

    def myPow(self, a, n):
        return 1/self.binpow(a, abs(n)) if n < 0 else self.binpow(a, n) 
 

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def function(base, exponent):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return function(base * base, exponent // 2)
            else:
                return base * function(base * base, (exponent - 1) // 2)

        f = function(x, abs(n))
        
        return float(f) if n >= 0 else 1/f

# https://cp-algorithms.com/algebra/binary-exp.html 
class Solution:
    def binpow(self, a, n):
        ans = 1
        while n:
            if n & 1:
                ans *= a
            a*=a
            n >>=1
        return ans 
    
    def myPow(self, x: float, n: int) -> float:
        is_neg = True if n <0 else False
        n = abs(n)
        
        return 1/self.binpow(x, n) if is_neg else self.binpow(x, n)
       

        

class Solution:
    def binpow(self, a, n):
        res = 1
        while n:
            if n % 2 == 1:
                res *= a
            a = a * a
            n //= 2

        return res


    def myPow(self, a, n):
        return 1/self.binpow(a, abs(n)) if n < 0 else self.binpow(a, n) 
        
class Solution:
    def binpow(self, a, n):
        res = 1
        tmp = a
        while n:
            if n % 2 == 1:
                res *= tmp
            tmp = tmp * tmp
            n //= 2

        return res
