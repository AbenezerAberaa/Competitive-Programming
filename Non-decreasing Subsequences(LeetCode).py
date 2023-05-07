class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        length = len(nums)
        sets = set()

        def find(index, last, current):
            if index == length:
                if len(current) >= 2:
                    sets.add(tuple(current))
                return
            if nums[index] >= last:
                current.append(nums[index])
                find(index+1, nums[index], current)
                current.pop()
            find(index+1, last, current)
        find(0, -10000, [])
        return sets
