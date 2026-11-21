class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 空間 O(n)：残した区間をリストで持つ
        # intervals.sort()
        # rest = []
        # for s, e in intervals:
        #     if rest and s < rest[-1][1]:
        #         rest[-1][1] = min(rest[-1][1], e)
        #     else:
        #         rest.append([s, e])
        
        # return len(intervals) - len(rest)

        # 空間 O(1)：prev と count だけ持つ（時間はどれも O(n log n)）
        # intervals.sort()
        # count = 0
        # prev = []
        # for s, e in intervals:
        #     if prev and s < prev[1]:
        #         prev[1] = min(prev[1], e)
        #         count += 1
        #     else:
        #         prev = [s, e]
        
        # return count
        
        # 時間 O(n log n)、空間 O(1)：使うのは end だけなので数値で持つ
        intervals.sort()
        count = 0
        prev_end = float("-inf")
        for s, e in intervals:
            if s < prev_end:
                prev_end = min(prev_end, e)
                count += 1
            else:
                prev_end = e
        
        return count

