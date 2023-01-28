class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        
        max_sums = sum(nums[:k])
        curr_sum = sum(nums[:k])
        for right in range(k,len(nums)):
            curr_sum += nums[right] - nums[right-k]
            max_sums = max(max_sums, curr_sum)
        return max_sums / k
