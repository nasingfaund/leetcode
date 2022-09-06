class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return False
        if n == 1:
            return 1
        
        k = [0]*n
        k[0] = 1
        p1 = p2 = p3 = 0
        
        for i in range(1, n):
            k[i] = min(k[p1]*2, k[p2]*3, k[p3]*5)
            if k[i] == k[p1]*2:
                p1 += 1
            if k[i] == k[p2]*3:
                p2+=1
            if k[i] == k[p3]*5:
                p3+=1
        return k[n-1]
