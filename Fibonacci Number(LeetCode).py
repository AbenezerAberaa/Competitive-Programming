class Solution:
    def fib(self, n: int) -> int:
        #RECURSIVE APPROACH
        '''if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1)+self.fib(n-2)'''
        #ITERATIVE APPROACH
        if n == 0:
            return 0
        if n == 1:
            return 1

        prev1 = 0
        prev2 = 1
        result = 0
        for index in range(2,n+1):
            result = prev1 + prev2
            prev1 = prev2
            prev2 = result
        return result
