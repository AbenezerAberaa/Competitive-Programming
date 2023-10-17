class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:

        maxu, minu = max(nums), min(nums)
        
        diff = maxu - minu
        
        if 2*k >= diff:
            return 0
        return diff - 2*k
        
