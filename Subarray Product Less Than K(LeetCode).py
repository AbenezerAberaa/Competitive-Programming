class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        count = 0
        pro_so_far = 1
        for right in range(len(nums)):
            pro_so_far *= nums[right]
            while pro_so_far >= k:
                pro_so_far /= nums[left]
                left += 1
            count += (right - left + 1)
            
        return count
