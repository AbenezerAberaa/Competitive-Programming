class Solution:
    def knightDialer(self, n: int) -> int:

        memo = [[-1 for _ in range(10)] for _ in range(n + 1)] 
        d = {0:[4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4:[0,3,9], 6:[0,1,7], 7:[2,6], 8:[1,3], 9:[2,4], 5:[]}
    
        def countCombinations(currP, N):
            if memo[currP][N] != -1: return memo[currP][N]
            if n == currP: return 1
            count = 0
            
            for i in d[N]:
                count += countCombinations(currP + 1, i)
            
            memo[currP][N] = count
            return count
        
        count = 0
        for i in range(10):
            count += countCombinations(1, i)
        
        return (count%(10**9 + 7))
        
