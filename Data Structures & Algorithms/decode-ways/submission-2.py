class Solution:
    def numDecodings(self, s: str) -> int:
        seen = {}

        def f(i):
            if i == -1:
                return 1
            if i == 0:
                if s[0] != "0":
                    return 1
                return 0
            if i in seen:
                return seen[i]

            total = 0
            if s[i] != "0":
                total += f(i - 1)
            if 10 <= int(s[i-1:i+1]) <= 26:
                total += f(i - 2)

            seen[i] = total

            return seen[i]

        return f(len(s) - 1)