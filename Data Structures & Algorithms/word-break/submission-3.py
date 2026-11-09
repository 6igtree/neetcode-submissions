class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        LENGTH = len(s)
        memo = {}
        
        def f(i):
            if i == LENGTH:
                return True
            if i in memo:
                return memo[i]
            
            res = False
            for w in wordDict:
                if s[i:i + len(w)] == w:
                    res = res or f(i + len(w))
            
            memo[i] = res

            return memo[i]

        return f(0)


