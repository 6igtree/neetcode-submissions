import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        res = []
        for i in range(k):
            res.append(c.most_common()[i][0])
        return res
            
         
