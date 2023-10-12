class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @cache
        def recursiveFn(nums, gcdIndex):
            score = 0
            for i in range(len(nums)):
                x = nums[i]
                for j in range(i+1, len(nums)):
                    y = nums[j]
                    reducedNums = tuple(nums[:i] + nums[i+1:j] + nums[j+1:])
                    score = max(score, gcdIndex*gcd(x, y)+recursiveFn(reducedNums, gcdIndex+1))
            return score
        maxScore = recursiveFn(tuple(nums), 1)
        
        return maxScore
