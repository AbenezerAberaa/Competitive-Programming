class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:

        minu = [nums[0]]
        for i in range(1, len(nums)):
            minu.append(minu[i - 1] & nums[i])
            
        abs_min = minu[-1]
        
        if abs_min > 0:
            return 1
        
        result = 1
        curr = nums[-1]
        i = len(nums) - 1
        while i > 0:
            if curr == abs_min and minu[i - 1] == abs_min:
                result += 1
                curr = nums[i - 1]
            else:
                curr &= nums[i - 1]
            i -= 1
        return result
