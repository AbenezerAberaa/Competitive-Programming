class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        sets = set(nums)
        for index in range(len(nums)+1):
            if index+1 not in sets:
                return index+1
