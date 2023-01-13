class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        remain = k % len(nums)

        def revers(first_part, second_part):
            while first_part < second_part:
                nums[first_part], nums[second_part] = nums[second_part], nums[first_part]
                first_part += 1
                second_part -= 1

        nums.reverse()
        revers(0, remain - 1)
        revers(remain, len(nums) - 1)
