class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float("inf")
        seen = {}
        for c in coins:
            seen[c] = 1

        def dp(a):
            if a == 0: return 0
            if a in seen: return seen[a]

            res = INF
            for c in coins:
                if (a - c) >= 0:
                    res = min(1 + dp(a - c), res)

            seen[a] = res
            
            return seen[a]

        res = dp(amount)

        return res if res != INF else -1