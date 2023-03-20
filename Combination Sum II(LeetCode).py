class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        
        candidates.sort()                      
        result = []
        def combination(nums, start, path, result, target):
            if not target:
                result.append(path)
                return
            for index in range(start, len(nums)):
                if index > start and nums[index] == nums[index - 1]:
                    continue
                if nums[index] > target:
                    break
                combination(nums, index + 1, path + [nums[index]], result, target - nums[index])
        combination(candidates, 0, [], result, target)
        return result
