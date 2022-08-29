# this problem is similar to https://stackoverflow.com/questions/57779421/calculating-all-possible-ways-to-score-in-a-football-game-recursively

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def helper(target, curr, candidates):
            if target == 0:
                result.append(curr[:])
                return
            if target < 0:
                return 
            for i in range(len(candidates)):
                curr.append(candidates[i])
                helper(target - candidates[i], curr, candidates[i:])
                curr.pop()
        
        helper(target, [], candidates)
        return result 
