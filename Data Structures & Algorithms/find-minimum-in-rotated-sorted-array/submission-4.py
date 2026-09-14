class Solution:
    def findMin(self, nums: List[int]) -> int:
        # num[n - 1] > num[n]になっている場所を探す

        # 1. O(n)の実装
        # for i in range(len(nums)):
        #     if  (i > 0) and (nums[i - 1] > nums[i]):
        #         return nums[i]
        # return nums[0]

        # 2. O(log n)の実装
        l, r = 0, len(nums) - 1

        while l < r: 
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]
