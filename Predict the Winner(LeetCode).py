class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def recurser(left, right):
            if left == right:
                return nums[left]
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            score = max(nums[right] - recurser(left, right-1), nums[left] - recurser(left+1, right))
            memo[(left, right)] = score
            
            return score
            
        memo = {}            
        return recurser(0, len(nums)-1) >= 0
