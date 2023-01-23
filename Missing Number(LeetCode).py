class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        sums = int((len(nums)*(len(nums)+1)) // 2)
        for value in nums:
            sums -= value
        if sums >= 0:
            return sums
        if sums < 0:
            return -(sums)
