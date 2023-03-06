class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        if target not in nums:
            return [-1,-1]
        right = bisect.bisect_right(nums, target)
        left = bisect.bisect_left(nums, target)
        return[left, right-1]
