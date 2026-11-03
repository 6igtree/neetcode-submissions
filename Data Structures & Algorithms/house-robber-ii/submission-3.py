class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_line(houses):
            seen = {}
            def dp(i):
                if i == 0:
                    return houses[0]
                elif i == 1:
                    return max(houses[0], houses[1])
                elif i not in seen:
                    seen[i] = max(dp(i-1), houses[i] + dp(i-2))

                return seen[i]

            return dp(len(houses) - 1)
        
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        return max(rob_line(nums[1:]), rob_line(nums[:len(nums)-1]))