class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # return sum(range(len(nums) + 1)) - sum(nums)
        # Bit Manipulation
        res = 0
        for i in range(len(nums) + 1):
            res = res ^ i

        for n in nums:
            res = res ^ n
        
        # 2進数と10進数でbit演算できる
        # print(1 ^ 0b10)
        # print(0b01 ^ 0b10)

        return res