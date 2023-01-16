class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        for index in range(1, len(nums)): 
            nums[index] += nums[index - 1]
        result, firstMax, secondMax = nums[firstLen + secondLen - 1], nums[firstLen - 1], nums[secondLen - 1]
        for index in range(firstLen + secondLen, len(nums)): 
            firstMax = max(firstMax, nums[index - secondLen] - nums[index - firstLen - secondLen])
            secondMax = max(secondMax, nums[index - firstLen] - nums[index - firstLen - secondLen])
            result = max(result, firstMax + nums[index] - nums[index - secondLen], secondMax + nums[index] - nums[index - firstLen])
        return result
