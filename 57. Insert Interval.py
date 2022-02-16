class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []

        i, start, end = 0, 0, 1

        # skip (and add to output) all intervals that come before the 'new_interval'
        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            merged.append(intervals[i])
            i += 1

        # merge all intervals that overlap with 'new_interval'
        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(intervals[i][start], newInterval[start])
            newInterval[end] = max(intervals[i][end], newInterval[end])
            i += 1

        # insert the new_interval
        merged.append(newInterval)

        # add all the remaining intervals to the output
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        return merged
