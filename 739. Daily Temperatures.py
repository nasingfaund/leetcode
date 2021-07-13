# brute force O(n^2), time limit execution
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            counter = 0
            for j in range(i+1, len(temperatures)):
                counter +=1
                if temperatures[j] > temperatures[i]:
                    res.append(counter)
                    counter = 0
                    break
                
            if counter != 0:
                res.append(0)
        res.append(0)
        return res
      
      
      
# using Monotonic Stack     
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in temperatures]
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            ans[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return ans
