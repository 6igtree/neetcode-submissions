class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)

        path = set()

        def dfs(c):
            if c in path:
                return False
            path.add(c)
            for pre in adj[c]:
                if not dfs(pre):
                    return False
            path.remove(c)
            adj[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True