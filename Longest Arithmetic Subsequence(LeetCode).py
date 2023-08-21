class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        dicts = {}
        for indx in range(len(nums)):
            for j in range(indx+1, len(nums)):
                diff = nums[j] - nums[indx]
                dicts[j, diff] = dicts.get((indx, diff), 1) + 1
        return max(dicts.values())
