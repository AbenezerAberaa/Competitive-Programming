class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        dp_set = set()
        dp_set.add(0)
        for index in range(len(nums)-1, -1, -1):
            next_dp_set = set()
            for if_target in dp_set:
                next_dp_set.add(nums[index] + if_target)
                next_dp_set.add(if_target)
            dp_set = next_dp_set
        return True if target in dp_set else False
