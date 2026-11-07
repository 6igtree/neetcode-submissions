class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            return [l + 1, r - 1]

        for i in range(len(s)):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i + 1)

            if len(res) < r1 - l1 + 1:
                res = s[l1:r1 + 1]

            if len(res) < r2 - l2 + 1:
                res = s[l2:r2 + 1]

        return res