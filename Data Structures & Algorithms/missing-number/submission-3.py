class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # return sum(range(len(nums) + 1)) - sum(nums)
        # Bit Manipulation
        res = 0
        for i in range(len(nums) + 1):
            res = res ^ i
        
        print(res)
        # print(1 ^ 0b10)
        # print(0b01 ^ 0b10)

        return sum(range(len(nums) + 1)) - sum(nums)