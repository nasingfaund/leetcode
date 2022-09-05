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
    
# clerer dfs 
class Solution:
    def lastStoneWeightII(self, A, s=0, index=0):
        @cache
        def find(s=0, index=0):
            if index >= len(A):
                return float('inf') if s < 0 else s
            add = find(s + A[index], index + 1)
            sub = find(s - A[index], index + 1)
            
            return min(add, sub)
        return find(0, 0)


    
# brute force
# time: O(n*sum)
# space O(sum)
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        aset = {0}
        for stone in stones:
            new_set = set()
            for elem in aset:
                new_set.add(elem - stone)
                new_set.add(elem + stone)
            aset = new_set
        return min(map(abs, aset))
                
        
