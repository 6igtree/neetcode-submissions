class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        path = []

        def dfs(start, remain):
            if remain == 0:
                res.append(path.copy())
                return
            if remain < 0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, remain - candidates[i])
                path.pop()

        dfs(0, target)
        return res