from collections import Counter

class Solution:
    # def isAnagram(self, s: str, t: str:)
    #     return Counter(s) == Counter(t)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in cnt:
                cnt[sorted_s].append(s)
            else:
                cnt[sorted_s] = [s]
                
        return [v for i, (k, v) in enumerate(cnt.items())]
