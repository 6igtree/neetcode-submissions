from collections import defaultdict
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            # cnt = Counter(s)
            # for i in range(cnt):
            #     print(cnt[i])
            tmp = "".join(sorted(s))
            groups[tmp].append(s)
        return list(groups.values())
