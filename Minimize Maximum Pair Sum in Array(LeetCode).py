class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxu = float("-inf")
        for i in range(len(nums) // 2):
            maxu = max(maxu, nums[i] + nums[len(nums) - 1 - i])
        return maxu
