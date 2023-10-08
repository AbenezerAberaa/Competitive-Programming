class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        def helper(i,j):
            if i >= n:
                return 0
            if (i,j) in cache:
                return cache[i,j]

            take = satisfaction[i]*j + helper(i+1,j+1)
            notTake = 0 + helper(i+1,j)
            cache[i,j] = max(take,notTake)
            return cache[i,j]

        n = len(satisfaction)
        satisfaction.sort()
        cache = {}
        return helper(0,1)
