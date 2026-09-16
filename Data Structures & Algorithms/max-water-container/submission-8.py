class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 不変条件（invariant）
        # 自分より高い棒がなければ、内側に動かしてはいけない
        l, r = 0, len(heights) - 1
        largest = 0
        while l < r:
            w = r - l
            h = min(heights[r], heights[l])
            largest = max(w * h, largest)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return largest

            








        
            
