class Solution:
    def countBits(self, n: int) -> List[int]:
        def ones(x):
            count = 0
            while x:
                count += x & 1
                x >>= 1
            return count
        return [ones(i) for i in range(n + 1)]

