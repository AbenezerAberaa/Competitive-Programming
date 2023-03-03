class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        for presum in range(1,len(nums)):
            nums[presum] += nums[presum-1]
        return nums
