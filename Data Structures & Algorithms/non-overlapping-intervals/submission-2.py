class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # O(n)の解法
        # intervals.sort()
        # rest = []
        # for s, e in intervals:
        #     if rest and s < rest[-1][1]:
        #         rest[-1][1] = min(rest[-1][1], e)
        #     else:
        #         rest.append([s, e])
        
        # return len(intervals) - len(rest)

        # O(1)の解法
        intervals.sort()
        count = 0
        prev = []
        for s, e in intervals:
            if prev and s < prev[1]:
                prev[1] = min(prev[1], e)
                count += 1
            else:
                prev = [s, e]
        
        return count

