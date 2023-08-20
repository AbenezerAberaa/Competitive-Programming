class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return len(nums)

        to_min = 1
        to_max = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                to_max = to_min +1
            elif nums[i] < nums[i-1]:
                to_min = to_max + 1
            
        return max(to_min, to_max)
