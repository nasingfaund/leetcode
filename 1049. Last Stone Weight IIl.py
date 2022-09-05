class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        self.result = float('inf')
        @cache
        def find(index, s):
            print(index)
            if index >= len(stones):
                self.result = min(self.result, abs(s))
                return s
            
            add = find(index + 1, s + stones[index])
            sub = find(index + 1, s - stones[index])
                
            return add + sub
        
        find(0, 0)
        return self.result
