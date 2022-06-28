# greedy solution, O(n)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x: x[1])
        prev = float('-inf')
        for i in range(len(intervals)):
            if intervals[i][0] >= prev:
                prev = intervals[i][1]
            else:
                count +=1
        return count
        
