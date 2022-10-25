class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        currentSum = 0
        prefixSumDict = {0 : 1}
        for value in nums:
            currentSum += value
            difference = currentSum - k
            count += prefixSumDict.get(difference, 0)
            prefixSumDict[currentSum] = prefixSumDict.get(currentSum, 0) + 1
        return count
            
            