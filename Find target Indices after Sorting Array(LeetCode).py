class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        beginIndex = 0
        endIndex = 0
        for n in nums:
            if n < target:
                beginIndex += 1
            elif n == target:
                endIndex += 1
        return (list(range(beginIndex,beginIndex+endIndex)))
        