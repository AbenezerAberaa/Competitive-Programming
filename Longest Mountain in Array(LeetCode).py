class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        """
        :type arr: List[int]
        :rtype: int
        """
        result = 0
        maxLen = 0
        minLen = 0
        for i in range(1, len(arr)):
            if (minLen and arr[i-1] < arr[i]) or arr[i-1] == arr[i]:
                maxLen = 0
                minLen = 0
            maxLen += arr[i-1] < arr[i]
            minLen += arr[i-1] > arr[i]
            if maxLen and minLen:
                result = max(result, maxLen+minLen+1)
        return result
        