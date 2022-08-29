class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, path):
            if len(path) == k:
                res.append(path[:])
                return
            
            for j in range(i, n):
                path.append(j + 1)
                backtrack(j + 1, path)
                path.pop()

        backtrack(0, [])
        return res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        alist = list(range(1, n+1))
        result = []
        stack = [[alist, [], k]]
        while stack:
            a, curr, k = stack.pop()
            if k == 0:
                result.append(curr)
            else:
                for i in range(len(a)):
                    stack.append([a[i+1:], curr + [a[i]], k - 1])
        return result

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def gen_k_comb(alist, k):
            for i in range(len(alist)):
                if k == 1:
                    yield (alist[i],)
                else:
                    for comb in gen_k_comb(alist[i + 1:], k - 1):
                        yield (alist[i],) + comb


        yield from gen_k_comb(list(range(1, n+1)), k)
