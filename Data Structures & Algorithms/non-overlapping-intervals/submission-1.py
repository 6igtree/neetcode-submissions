class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rest = []
        for s, e in intervals:
            if rest and s < rest[-1][1]:
                rest[-1][1] = min(rest[-1][1], e)
            else:
                rest.append([s, e])
        
        return len(intervals) - len(rest)