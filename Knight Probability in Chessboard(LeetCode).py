class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:


        dp = dict()
        def my_function(row,column,move) -> int:
            
            if (row,column,move) in dp:
                return dp[(row,column,move)]
            if row < 0 or column < 0 or row > n-1 or column > n-1:
                return 0
            if move == 0:
                return 1
            moves = [(-2,-1),(-1,-2),(-2,1),(-1,2),(2,-1),(1,-2),(2,1),(1,2)]
            ans = 0
            for x in moves:
                ans += my_function(row+x[0],column+x[1],move-1)/8
            dp[(row,column,move)] = ans
            return ans

        return my_function(row,column,k)
