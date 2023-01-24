class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        first2Last1 = nums[0]*nums[1]*nums[-1] 
        last3 = nums[-1]*nums[-2]*nums[-3]
        maxu = max(first2Last1,last3)
        return maxu
