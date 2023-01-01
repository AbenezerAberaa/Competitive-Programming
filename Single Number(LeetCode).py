class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        for value in nums:
            if nums.count(value) == 1:
                return value

