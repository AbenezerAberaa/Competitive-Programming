class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr.sort()
        maxu = arr[0] = 1
        for i, num in enumerate(arr):
            if num > maxu:
                maxu += 1
        return maxu
