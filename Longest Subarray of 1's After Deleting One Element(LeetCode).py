class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        left = 0
        for right in range(len(nums)):
            counter += (nums[right] == 0)
            if counter >= 2:
                counter -= (nums[left] == 0)
                left += 1
        return (right - left + 1) - 1
