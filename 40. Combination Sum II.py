class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def helper(curr, target, index):
            if target == 0:
                result.append(curr[:])
                return
            if target < 0:
                return 
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                helper(curr, target - candidates[i], i + 1)
                curr.pop()
        helper([], target, 0)
        return result
