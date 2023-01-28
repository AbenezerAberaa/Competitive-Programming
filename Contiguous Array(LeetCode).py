class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        dic = {}
        sums = 0
        long_subArr = 0
        for index in range(len(nums)):
            if nums[index] == 1:
                sums = sums + 1
            else:
                sums = sums - 1

            if sums == 0:
                long_subArr = index + 1
            elif sums not in dic:
                dic[sums] = index
            elif long_subArr < index - dic[sums]:
                long_subArr = index - dic[sums]
        return long_subArr
