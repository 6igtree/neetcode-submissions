class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ns, ne = newInterval
        res = []
        for i in range(len(intervals)):
            s, e = intervals[i]
            if e < ns:
                res.append([s, e])
            elif ne < s:
                res.append([ns, ne])
                return res + intervals[i:]
            else:
                ns, ne = min(s, ns), max(e, ne)
        res.append([ns, ne])
        
        return res
