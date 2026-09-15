class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n)で解く
        best = 0
        for l in range(len(prices)):
            r = l + 1
            while r < len(prices):
                best = max(prices[r] - prices[l], best)
                r += 1

        return best