class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, seen, prev_height):
            if r < 0 or r > ROWS - 1 or c < 0 or c > COLS - 1 or (r, c) in seen or heights[r][c] < prev_height:
                return

            seen.add((r, c))

            dfs(r + 1, c, seen, heights[r][c])
            dfs(r, c + 1, seen, heights[r][c])
            dfs(r - 1, c, seen, heights[r][c])
            dfs(r, c - 1, seen, heights[r][c])


        pac, atl = set(), set()
        for c in range(COLS):
            dfs(0, c, pac, 0)
            dfs(ROWS - 1, c, atl, 0)
        for r in range(ROWS):
            dfs(r, 0, pac, 0)
            dfs(r, COLS - 1, atl, 0)
        
        return [[r, c] for (r, c) in pac & atl]