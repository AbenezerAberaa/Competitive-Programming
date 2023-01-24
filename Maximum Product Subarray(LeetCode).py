class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxu = nums[0]
        currMin, currMax = 1, 1
        for n in nums:
            if n < 0:
                currMax, currMin = currMin, currMax
            
            currMax = max(n, n * currMax)
            currMin = min(n, n * currMin)
            maxu = max(maxu, currMax)
        
        return maxu
