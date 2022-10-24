class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        array_sum = sum(nums)
        
        
        for index in range(0,len(nums)):
            right_sum = array_sum - left_sum - nums[index]
            if right_sum == left_sum:
                return index
            left_sum = left_sum + nums[index]
            
        return -1
                
            
        
        