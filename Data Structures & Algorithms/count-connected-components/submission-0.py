class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        seen = set()
        count = 0

        def dfs(edge):
            if edge in seen:
                return

            seen.add(edge)

            for a in adj[edge]:
                dfs(a)


        for i in range(n):
            if not i in seen:
                dfs(i)
                count = count + 1

        
        
        return count