class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(n):
            if n == 1 or n == 0:
                return 1

            if n - 1 not in memo:
                memo[n - 1] = dp(n - 1)
            if n - 2 not in memo:
                memo[n - 2] = dp(n - 2)

            return memo[n - 1] + memo[n - 2]

        return dp(n)