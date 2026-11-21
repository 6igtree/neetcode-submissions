class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # [[1,10],[2,3],[4,5]]   正解は 1
        rest = []
        for s, e in intervals:
            if rest and s < rest[-1][1]:
                rest[-1][1] = min(rest[-1][1], e)
            else:
                rest.append([s, e])
        
        return len(intervals) - len(rest)