from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)] 
        for n, freq in count.items():
            bucket[freq].append(n)
        res = []
        for freq in range(len(bucket) - 1, 0, - 1):
            for n in bucket[freq]:
                res.append(n)
                if len(res) == k:
                    return res
            
            
            
         
