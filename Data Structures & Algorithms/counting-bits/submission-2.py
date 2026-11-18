class Solution:
    def countBits(self, n: int) -> List[int]:
        # O(n)の回答
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res
        
        # def ones(x):
        #     count = 0
        #     while x:
        #         count += x & 1
        #         x >>= 1
        #     return count
        # return [ones(i) for i in range(n + 1)]

