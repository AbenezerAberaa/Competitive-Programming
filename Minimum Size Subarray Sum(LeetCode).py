class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = 0
        minLength = math.inf
        currentSum = 0
    
        for i in range(len(nums)):
            currentSum += nums[i]
            while currentSum >= target:
                minLength = min(minLength, i - count + 1)
                currentSum -= nums[count]
                count += 1
                
        if minLength == math.inf:
            return 0
        else:
            return minLength
        
            
                
                    
                
                
                
        