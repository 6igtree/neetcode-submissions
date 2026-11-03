class Solution:
    def rob(self, nums: List[int]) -> int:
        seen = {}

        def dp(i):
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[0], nums[1])
            elif i not in seen:
                seen[i] = max(dp(i-1), nums[i] + dp(i-2))

            return seen[i]
        
        return dp(len(nums)-1)