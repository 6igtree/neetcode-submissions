class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n^2)で解く
        # best = 0
        # for l in range(len(prices)):
        #     r = l + 1
        #     while r < len(prices):
        #         best = max(prices[r] - prices[l], best)
        #         r += 1
        # O(n)で解く
        lowest = prices[0]
        max_profit = 0
        l, r = 0, 1
        while r < len(prices):
            lowest = min(lowest, prices[l])
            max_profit = max(prices[r] - lowest, max_profit)
            l += 1
            r += 1

        return max_profit