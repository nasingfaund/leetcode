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
