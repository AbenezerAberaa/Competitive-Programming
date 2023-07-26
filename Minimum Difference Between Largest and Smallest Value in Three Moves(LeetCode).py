class Solution:
    def minDifference(self, nums: List[int]) -> int:

        nums.sort()
        if(len(nums))>3:
            s = nums[-1]-nums[0]
            a = nums[-1]-nums[3]
            b = nums[-2]-nums[2]
            c = nums[-3]-nums[1]
            d = nums[-4]-nums[0]
    
            return min(s,a,b,c,d) 
        else:
            return 0
