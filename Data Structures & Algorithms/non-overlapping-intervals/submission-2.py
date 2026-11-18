class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        last = intervals[0][1]
        removed = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= last:
                last = intervals[i][1]
            else:
                removed += 1
                last = min(last, intervals[i][1])
        return removed