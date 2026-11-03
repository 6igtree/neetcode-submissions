class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        seen = set()

        def dfs(child, parent):
            if child in seen:
                return False

            seen.add(child)

            for nei in adj[child]:
                if nei == parent:
                    continue
                if not dfs(nei, child):
                    return False

            return True

        return dfs(0, -1) and len(seen) == n
