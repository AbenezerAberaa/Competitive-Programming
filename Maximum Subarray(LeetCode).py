class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_so_far = nums[0]
        max_curr = nums[0]

        for index in range(1, len(nums)):
            max_curr = max(max_curr+nums[index], nums[index])
            max_so_far = max(max_curr, max_so_far)

        return max_so_far

