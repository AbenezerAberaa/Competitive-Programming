class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        l = len(nums)
        remainders_dict = {0:1}
        pre = 0
        total = 0
        for index in range(l):
            pre += nums[index]
            rem = pre % k
            remainders_dict.setdefault(rem,0)
            total += remainders_dict[rem]
            remainders_dict[rem]+=1
            
        return total
