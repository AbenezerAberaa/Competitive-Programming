class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        new_list1 = nums[1:]
        new_list2 = nums[:-1]
        return max(self.result(new_list1), self.result(new_list2))
    
    def result(self, new_list: List[int]) -> int:
        first, second = 0, 0
        for x in new_list:
            temp = max(first + x, second)
            first = second
            second = temp
        return second
