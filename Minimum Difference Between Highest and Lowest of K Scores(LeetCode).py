class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        minDif=float('inf')
        
        left = 0
        for right in range(k-1,len(nums)):
            curd=nums[right]-nums[left]
            minDif=min(minDif,curd)
            left += 1
        return minDif
