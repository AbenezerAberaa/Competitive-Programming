class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        sets = set(nums)
        arr = []
        for index in range(len(nums)):
            if index+1 not in sets:
                arr.append(index+1)
        return arr
