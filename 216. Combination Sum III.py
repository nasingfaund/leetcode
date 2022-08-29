class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        all_combinations = list(combinations(range(1,10), k))
        sum_n = [c for c in all_combinations if sum(c)==n]
        return sum_n
    
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res  = []
        def helper(curr, target, k, index):
            if target == 0 and len(curr) == k:
                res.append(curr[:])
                return 
            if len(curr) == k:
                return 
            for i in range(index, 10):
                curr.append(i)
                helper(curr, target - i, k, i + 1)
                curr.pop()
                
        helper([], n, k, 1)
        return res
                            
