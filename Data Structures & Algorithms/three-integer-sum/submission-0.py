class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3 <= nums.length <= 3000
        # -10^5 <= nums[i] <= 10^5
        # -> O(n^2)ならOK

        
        # O(nlogn)
        # before: [-1, 0, 1, 2, -1, -4]
        # after: [-4, -1, -1, 0, 1, 2]
        # -(-4) > -1 + 2
        # -> 右辺を大きする
        nums = sorted(nums)

        # nums[j] + nums[k] + nums[i] = 0
        res = []

        # O(n)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            # O(n)
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                
                if total <= 0:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif total > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res