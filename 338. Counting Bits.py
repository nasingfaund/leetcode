class Solution:
    def countBits(self, num: int) -> List[int]:
        counter = [0]
        for i in range(1, num+1):
            result = [1..5]
            counter.append(counter[i >> 1] + i % 2)
        return counter

class Solution:
    def countBits(self, num):
        cache = {}

        def f(num: int) -> int:
            if num in cache:
                return cache[num]
            if num == 0:
                return 0
            cache[num] = f(num >> 1) + num % 2
            return cache[num]

        result = []
        for i in range(0, num + 1):
            result.append(f(i))
        return result

