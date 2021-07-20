class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for row in mat:
            res.append(row.count(1))
        res = enumerate(res)
        return [o[0] for o in sorted(res, key=lambda x: x[1])][:k]
        
