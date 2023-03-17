class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        answer = []

        def backtracker(candidate, candidate_sum, index):
            if candidate_sum == target:
                answer.append(candidate[:])
                return
            if index  == len(nums) or target-candidate_sum < nums[index]:
                return

            candidate.append(nums[index])
            backtracker(candidate, candidate_sum+nums[index], index)
            candidate.pop()
            backtracker(candidate, candidate_sum, index+1)
        nums = sorted(nums)
        backtracker([], 0, 0)
        return  answer
