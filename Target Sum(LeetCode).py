class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp_dict = {}
        def backtrack(indx,total):
            if indx == len(nums):
                return 1 if target==total else 0
            if (indx,total) in dp_dict:
                return dp_dict[(indx,total)]
            dp_dict[(indx,total)]=backtrack(indx+1,total+nums[indx])+backtrack(indx+1,total-nums[indx])
            return dp_dict[(indx,total)]
        return backtrack(0,0)
