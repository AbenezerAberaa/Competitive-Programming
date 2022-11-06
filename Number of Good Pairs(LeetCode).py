class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict_cont = {}
        result = 0
        for value in nums:
            if value in dict_cont:
                result += dict_cont[value]
                dict_cont[value] += 1
            else:
                dict_cont[value] = 1
        return result
