class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for index, value in enumerate(nums):
            nums[index] = str(value)
        #nums = list(map(str, nums))
        print(nums)
        def do_comparision(x, y):
            if x+y > y+x:
                return -1
            else:
                return 1
        nums = sorted(nums, key=cmp_to_key(do_comparision))
        return str(int("".join(nums)))
