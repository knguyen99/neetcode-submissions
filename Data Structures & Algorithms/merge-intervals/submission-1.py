class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        ret = []
        ret.append(intervals[0])

        for i in range(1,len(intervals)):
            start, end = intervals[i]
            
            if start <= ret[-1][1]:
                ret[-1][1] = max(ret[-1][1], end)
            else:
                ret.append([start, end])
        return ret