class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxu  = reduce(lambda a, b: a | b, nums)
        nums.sort(reverse = True)
        length = len(nums)
        self.result = 0
        def backtrack(curr, traverse):
            if curr == maxu:
                self.result += 2**(length - traverse)
                return
            if length == traverse:
                return
            backtrack(curr, traverse+1)
            backtrack(curr | nums[traverse],traverse+1)
        backtrack(0,0)
        return self.result
