class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        seen = set()
        count = 0

        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)
            for a in adj[node]:
                dfs(a)
            
        for i in range(n):
            if i not in seen:
                dfs(i)
                count = count + 1

        return count