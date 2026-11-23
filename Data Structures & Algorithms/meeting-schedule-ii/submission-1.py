"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sl = sorted(i.start for i in intervals)
        el = sorted(i.end for i in intervals)

        res = 0
        count = 0
        s, e = 0, 0
        while s < len(sl):
            if sl[s] < el[e]:
                count += 1
                res = max(res, count)
                s += 1
            else:
                count -= 1
                e += 1

        return res
