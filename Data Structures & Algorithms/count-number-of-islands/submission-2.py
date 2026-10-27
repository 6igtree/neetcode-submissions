class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        seen = set()

        def dfs(r, c):
            if r < 0 or r > len(grid) - 1 or c < 0 or c > len(grid[0]) - 1 or (r, c) in seen or grid[r][c] == "0":
                return
            
            seen.add((r, c))

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
            
            return
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in seen:
                    dfs(r, c)
                    islands += 1

        return islands