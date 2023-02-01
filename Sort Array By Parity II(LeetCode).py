class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        left_even = 0
        right_odd = 1
        while left_even < len(nums) and right_odd < len(nums):
            while left_even < len(nums) and nums[left_even] % 2 == 0:
                left_even += 2
            while right_odd < len(nums) and nums[right_odd] % 2 != 0:
                right_odd += 2
            if left_even < len(nums) and right_odd < len(nums):
                nums[left_even], nums[right_odd] = nums[right_odd], nums[left_even]
            left_even += 2
            right_odd += 2
        return nums
