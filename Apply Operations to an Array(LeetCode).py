class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:


        for index in range(len(nums)-1):
            if nums[index] == nums[index+1]:
                nums[index] = nums[index]*2
                nums[index+1] = 0
        n = nums.count(0)
        print(nums)
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
            right += 1
        for index in range(left, len(nums)):
            nums[index] = 0
        
        return nums
