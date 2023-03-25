class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        pointer = 0
        while pointer < len(nums):
            corr_pos = nums[pointer]-1
            if nums[pointer] != nums[corr_pos]:
                nums[pointer], nums[corr_pos] = nums[corr_pos], nums[pointer]
            else:
                pointer += 1
        ans = []
        for index in range(len(nums)):
            if index != nums[index]-1:
                ans.append(nums[index])
        return ans
