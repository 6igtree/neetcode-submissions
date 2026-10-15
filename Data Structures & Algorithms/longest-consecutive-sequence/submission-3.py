class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in num_set:
            if n - 1 not in num_set:
                length = 0
                while length + n in num_set:
                    length += 1
                longest = max(longest, length)
        return longest
                    
        

