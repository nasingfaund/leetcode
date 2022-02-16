class Solution:
    def _merge(self, intervals):
        for i in range(len(intervals) - 1):
            first = intervals[i]
            second = intervals[i + 1]
            if first[0] <= second[1] and first[1] >= second[0]:

                merged_interval = [(min(first[0], second[0]), max(first[1], second[1]))]
                return self._merge(intervals[:i] + merged_interval + intervals[i+2:])
        return intervals

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        return self._merge(intervals)
                               
# O(nlog⁡n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
        
