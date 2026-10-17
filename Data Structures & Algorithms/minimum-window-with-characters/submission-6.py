from collections import Counter
class Solution:
    def includeAll(self, count_s: dict, count_t: dict) -> bool:
        return all(count_s.get(c, 0) >= n for c, n in count_t.items())
    
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        window = {}
        have, need = 0, len(count)
        l = 0
        res_len = float("inf")
        res_l, res_r = 0, 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in count and window[c] == count[c]:
                have += 1
            while have == need:
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res_l, res_r = l, r
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        return s[res_l:res_r + 1] if res_len != float("inf") else ""